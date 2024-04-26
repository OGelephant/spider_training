from playwright.sync_api import sync_playwright
import cv2
from urllib import request

def get_distance(background,gap):
    background = cv2.imread(background,0)

    gap = cv2.