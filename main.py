import sys

import cv2
import os
from skimage.metrics import structural_similarity as compare_ssim

sr_dir = os.listdir(sys.argv[0])
hr_dir = os.listdir(sys.argv[1])

psnr = 0.0
ssim = 0.0
n = 0

def to_grey(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for hr_image in hr_dir:
    for sr_image in sr_dir:
        if sr_image == hr_image:
            if (sr_image[-3:]) != 'jpg':
                continue
            compute_psnr = cv2.PSNR(cv2.imread('./ground_truth/' + sr_image), cv2.imread('./result/' + hr_image))
            compute_ssim = compare_ssim(to_grey(cv2.imread('./ground_truth/' + sr_image)),
                                        to_grey(cv2.imread('./result/' + hr_image)))
            psnr += compute_psnr
            ssim += compute_ssim
            n += 1
            if n%sys.argv[2] == 0:
                print("finish compute avarage [%d/%d]" % (n, len(hr_dir)))

psnr = psnr / n
ssim = ssim / n
print("average psnr = ", psnr)
print("average ssim = ", ssim)
