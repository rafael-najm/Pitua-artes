"""Acrescenta os ponteiros dourados do Relógio Imari num clipe de vídeo.

Os ponteiros (10h10, como na foto do site) são desenhados sobre a foto 03 do Relógio Imari no acervo
e levados para cada quadro do vídeo por uma homografia (SIFT + RANSAC). O eixo é depois ajustado
ao furo do mostrador encontrado no próprio quadro, e tudo é suavizado no tempo.
Uso: python ponteiros.py entrada.mp4 saida.mp4 [--teste t1,t2,...]
"""
import sys
import subprocess

import cv2
import numpy as np

from pathlib import Path
REF = str(Path(__file__).resolve().parent.parent / 'src/assets/pecas/relogio-imari/03.jpg')  # foto do site, já com os ponteiros
HUB = np.array([939.0, 1730.0])   # centro do furo do mostrador na foto de referência
D12 = 430.0                        # distância do eixo até a marca das 12h
# pontas dos ponteiros, relativas ao eixo (medidas na foto do site)
HORA = np.array([-217.0, -147.0])
MINUTO = np.array([343.0, -195.0])
RABO = np.array([-55.0, 35.0])
SS = 2  # supersample da camada dos ponteiros

# cores em BGR (OpenCV)
OURO_CLARO = (112, 201, 236)
OURO = (60, 152, 196)
OURO_ESCURO = (36, 104, 140)


def desenha_camada(shape):
    h, w = shape
    rgb = np.zeros((h * SS, w * SS, 3), np.uint8)
    a = np.zeros((h * SS, w * SS), np.uint8)
    c = HUB * SS

    def poli(pts, cor):
        p = np.round(np.array(pts)).astype(np.int32)
        cv2.fillPoly(rgb, [p], cor, lineType=cv2.LINE_AA)
        cv2.fillPoly(a, [p], 255, lineType=cv2.LINE_AA)

    def lamina(vet, larg, duas_cores=True):
        tip = c + vet * SS
        u = vet / np.linalg.norm(vet)
        n = np.array([-u[1], u[0]])
        wd = larg * SS
        base = c - u * wd * 0.15
        if duas_cores:  # bisel: metade clara, metade escura
            poli([base + n * wd / 2, tip, base], OURO_CLARO)
            poli([base - n * wd / 2, tip, base], OURO)
        else:
            poli([base + n * wd / 2, tip, base - n * wd / 2], OURO)

    lamina(HORA, 38)
    lamina(MINUTO, 32)
    lamina(RABO, 26, False)
    ci = tuple(np.round(c).astype(int))
    cv2.circle(rgb, ci, int(31 * SS), OURO_ESCURO, -1, cv2.LINE_AA)
    cv2.circle(a, ci, int(31 * SS), 255, -1, cv2.LINE_AA)
    cv2.circle(rgb, ci, int(27 * SS), OURO, -1, cv2.LINE_AA)
    cv2.circle(rgb, ci, int(12 * SS), OURO_CLARO, -1, cv2.LINE_AA)
    return rgb, a


def referencia():
    ref = cv2.imread(REF)
    g = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    h, w = g.shape
    yy, xx = np.mgrid[0:h, 0:w]
    mask = (((xx - HUB[0]) ** 2 + (yy - HUB[1]) ** 2) < (1.45 * D12) ** 2).astype(np.uint8) * 255
    # os ponteiros da foto ficam de fora (o vídeo não tem ponteiros)
    pol = np.zeros_like(g)
    hub_foto = np.array([927.0, 1717.0])
    for v, larg in ((HORA, 60), (MINUTO, 60), (RABO, 50)):
        cv2.line(pol, tuple(hub_foto.astype(int)), tuple((hub_foto + v).astype(int)), 255, larg)
    cv2.circle(pol, tuple(hub_foto.astype(int)), 60, 255, -1)
    mask[pol > 0] = 0
    sift = cv2.SIFT_create(nfeatures=6000)
    kp, des = sift.detectAndCompute(g, mask)
    return ref.shape[:2], kp, des, sift


# quatro cantos de um quadrado em volta do mostrador (não colineares), que definem a homografia
CTRL = np.float32([HUB + [-D12, -D12], HUB + [D12, -D12], HUB + [D12, D12], HUB + [-D12, D12]])


def eixo(cantos):
    """Posição do eixo e distância eixo–12h no quadro, dados os 4 cantos."""
    H = cv2.getPerspectiveTransform(CTRL, np.float32(cantos))
    p = cv2.perspectiveTransform(np.float32([HUB, HUB + [0, -D12]]).reshape(-1, 1, 2), H).reshape(-1, 2)
    return p[0], np.linalg.norm(p[1] - p[0])


def casa(frame, kp_r, des_r, sift, flann):
    g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp, des = sift.detectAndCompute(g, None)
    if des is None or len(kp) < 10:
        return None, 0
    m = flann.knnMatch(des_r, des, k=2)
    bons = [a for a, b in (x for x in m if len(x) == 2) if a.distance < 0.72 * b.distance]
    if len(bons) < 15:
        return None, len(bons)
    src = np.float32([kp_r[x.queryIdx].pt for x in bons])
    dst = np.float32([kp[x.trainIdx].pt for x in bons])
    H, inl = cv2.findHomography(src, dst, cv2.RANSAC, 4.0)
    n = int(inl.sum()) if inl is not None else 0
    if H is None or n < 20:
        return None, n
    c = cv2.perspectiveTransform(CTRL.reshape(-1, 1, 2), H).reshape(-1, 2)
    lados = [np.linalg.norm(c[k] - c[(k + 1) % 4]) for k in range(4)]
    if min(lados) < 10 or max(lados) / min(lados) > 2.0 or not cv2.isContourConvex(c.astype(np.float32)):
        return None, n
    return c, n


def furo(frame, hub, d12):
    """Procura o anel escuro do furo do mostrador perto de onde a homografia previu o eixo."""
    raio = 0.17 * d12
    jan = int(max(20, raio * 2.2))
    x0, y0 = int(hub[0]) - jan, int(hub[1]) - jan
    h, w = frame.shape[:2]
    if x0 < 0 or y0 < 0 or x0 + 2 * jan >= w or y0 + 2 * jan >= h or raio < 6:
        return None
    g = cv2.cvtColor(frame[y0:y0 + 2 * jan, x0:x0 + 2 * jan], cv2.COLOR_BGR2GRAY)
    g = cv2.GaussianBlur(g, (0, 0), max(1.0, raio / 15))
    cs = cv2.HoughCircles(g, cv2.HOUGH_GRADIENT, dp=1.2, minDist=jan, param1=80, param2=18,
                          minRadius=int(raio * 0.7), maxRadius=int(raio * 1.35))
    if cs is None:
        return None
    cx, cy, _ = cs[0][0]
    p = np.array([x0 + cx, y0 + cy])
    if np.linalg.norm(p - hub) > raio:
        return None
    return p


def suaviza(serie, k):
    pad = np.pad(serie, ((k // 2, k // 2),) + ((0, 0),) * (serie.ndim - 1), mode='edge')
    return np.stack([pad[j:j + k].mean(0) for j in range(len(serie))])


def main():
    ent, sai = sys.argv[1], sys.argv[2]
    teste = None
    if len(sys.argv) > 3 and sys.argv[3] == '--teste':
        teste = [float(t) for t in sys.argv[4].split(',')]
    shape, kp_r, des_r, sift = referencia()
    rgb_l, a_l = desenha_camada(shape)
    flann = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=64))
    cap = cv2.VideoCapture(ent)
    fps = cap.get(cv2.CAP_PROP_FPS)
    quadros = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        quadros.append(f)
    idx = list(range(len(quadros))) if teste is None else [min(len(quadros) - 1, int(t * fps)) for t in teste]
    pts, ns = {}, {}
    for i in idx:
        c, n = casa(quadros[i], kp_r, des_r, sift, flann)
        ns[i] = n
        if c is not None:
            pts[i] = c
    conhecidos = sorted(pts)
    if not conhecidos:
        sys.exit('nenhum quadro casou')
    # descarta saltos: escala ou posição muito diferentes da mediana dos vizinhos
    if teste is None:
        ex = [eixo(pts[i]) for i in conhecidos]
        pos = np.array([e[0] for e in ex])
        esc = np.array([e[1] for e in ex])
        bons = []
        for j, i in enumerate(conhecidos):
            viz = slice(max(0, j - 6), j + 7)
            me = np.median(esc[viz])
            mp = np.median(pos[viz], 0)
            if abs(esc[j] / me - 1) < 0.15 and np.linalg.norm(pos[j] - mp) < 0.25 * me:
                bons.append(i)
        conhecidos = bons
    print(f'{len(idx) - len(conhecidos)} de {len(idx)} quadros sem casamento confiável', file=sys.stderr)
    arr = np.array([pts[i] for i in conhecidos])
    todos = np.stack([np.stack([np.interp(idx, conhecidos, arr[:, p, c]) for c in range(2)], -1) for p in range(4)], 1)
    # ajusta o eixo ao furo do mostrador
    corr = np.full((len(idx), 2), np.nan)
    for j, i in enumerate(idx):
        hub, d12 = eixo(todos[j])
        p = furo(quadros[i], hub, d12)
        if p is not None:
            corr[j] = p - hub
    ok = ~np.isnan(corr[:, 0])
    print(f'furo encontrado em {ok.sum()} de {len(idx)} quadros', file=sys.stderr)
    if ok.sum() >= max(1, len(idx) // 5):
        xs = np.arange(len(idx))
        corr = np.stack([np.interp(xs, xs[ok], corr[ok, c]) for c in range(2)], -1)
        if teste is None:
            corr = suaviza(suaviza(corr, 9), 9)
        todos = todos + corr[:, None, :]
    if teste is None and len(idx) > 7:
        todos = suaviza(suaviza(todos, 5), 5)
    h, w = quadros[0].shape[:2]
    S = np.diag([1 / SS, 1 / SS, 1]).astype(np.float64)
    saidas = []
    for j, i in enumerate(idx):
        H = cv2.getPerspectiveTransform(CTRL, todos[j].astype(np.float32)) @ S
        cam = cv2.warpPerspective(rgb_l, H, (w, h), flags=cv2.INTER_AREA).astype(np.float32)
        al = cv2.warpPerspective(a_l, H, (w, h), flags=cv2.INTER_AREA).astype(np.float32) / 255
        d12 = eixo(todos[j])[1]
        desl = d12 * 0.012
        sombra = cv2.GaussianBlur(cv2.warpAffine(al, np.float32([[1, 0, desl * 0.5], [0, 1, desl]]), (w, h)),
                                  (0, 0), max(1.0, d12 * 0.008)) * 0.35
        f = quadros[i].astype(np.float32) * (1 - sombra[..., None])
        # um pouco de desfoque, para o ponteiro ter a mesma nitidez da filmagem
        sg = max(0.5, d12 / 430 * 0.8)
        cam = cv2.GaussianBlur(cam, (0, 0), sg)
        al3 = cv2.GaussianBlur(al, (0, 0), sg)[..., None]
        # a luz da cena: escurece o dourado na mesma medida que o mostrador está escurecido no quadro
        f = f * (1 - al3) + cam * 0.86 * al3
        saidas.append(np.clip(f, 0, 255).astype(np.uint8))
    if teste is not None:
        for j, im in enumerate(saidas):
            cv2.imwrite(f'{sai}_{j}.jpg', im)
        return
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{w}x{h}',
                          '-r', str(fps), '-i', '-', '-c:v', 'libx264', '-crf', '14', '-preset', 'fast',
                          '-pix_fmt', 'yuv420p', sai], stdin=subprocess.PIPE)
    for im in saidas:
        p.stdin.write(im.tobytes())
    p.stdin.close()
    p.wait()


if __name__ == '__main__':
    main()
