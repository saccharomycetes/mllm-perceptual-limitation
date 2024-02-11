from PIL import Image, ImageDraw, ImageFont
from typing import List, Tuple
import argparse
from tqdm import tqdm
import random
import os
from tqdm import tqdm

def draw_text(
        text: List[str], 
        img_size: Tuple[int, int], 
        font_size: List[int], 
        position: List[Tuple[int, int]]
    ) -> Image:

    img = Image.new('RGB', img_size, color='white')
    draw = ImageDraw.Draw(img)

    for t, f, p in zip(text, font_size, position):
        font = ImageFont.truetype("Arial.ttf", size=f)
        bbox = draw.textbbox(p, t, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # place of real topleft
        top_left = (p[0] - text_width / 2, p[1] - text_height / 2)
        
        # (bbox[0], bbox[1]) != top_left !!!
        bbox = draw.textbbox(top_left, t, font=font)
        vertial_difference = bbox[1] - top_left[1]

        # adapted topleft
        top_left = (top_left[0], top_left[1] - vertial_difference)
        draw.text(top_left, t, fill="black", font=font)
    return img

def generate_unique_numbers(digit_count, sample_size):
    seen = set()
    while len(seen) < sample_size:
        number = ''.join(str(random.randint(0, 9)) for _ in range(digit_count))
        if number not in seen:
            seen.add(number)
    return list(seen)

def create_quality_image(args):
    sample_rates = [2*r for r in range(1, 11)]
    font_size = 50
    ratios = [s/font_size for s in sample_rates]

    for number in tqdm(args.digit_set, desc="Creating images", ncols=100):
        ori_img = draw_text(
            text=number,
            img_size=(args.image_size, args.image_size),
            font_size=[font_size],
            position=[args.center_pos]
        )
        for r in ratios:
            this_img = ori_img.resize((int(args.image_size*r), int(args.image_size*r)), Image.LANCZOS).resize((args.image_size, args.image_size), Image.BICUBIC)
            this_img.save(f'{args.save_dir}/{number[0]}_{int(r*font_size)}.png')

def create_size_image(args):
    rates = [r/2 for r in range(2, 12)]
    for number in tqdm(args.digit_set, desc="Creating images", ncols=100):
        ori_img = draw_text(
                text=number,
                img_size=(args.image_size, args.image_size),
                font_size=[8],
                position=[args.center_pos]
            )
        for r in rates:
            this_img = ori_img.crop((args.image_size/2 - args.image_size/(2*r), args.image_size/2 - args.image_size/(2*r), args.image_size/2 + args.image_size/(2*r), args.image_size/2 + args.image_size/(2*r))).resize((args.image_size, args.image_size), Image.BICUBIC)
            this_img.save(f'{args.save_dir}/{number[0]}_{r}.png')


def create_position_image(args):
    variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    patch_num = args.patch_num // 2 if args.patch_size < 15 else args.patch_num
    patch_size = args.patch_size * 2 if args.patch_size < 15 else args.patch_size

    for number in tqdm(args.digit_set, desc="Creating images", ncols=100):
        eq_texts = [f'{var}={str}' for var, str in zip(variables, number)]
        for y in range(patch_num):
            for x in range(patch_num):
                position = patch_num * y + x
                rest_positions = random.sample([k for k in range(patch_num ** 2) if k != position], 10)
                coordinates = [(x, y)] + [(r % patch_num, r // patch_num) for r in rest_positions]
                corrdinates = [(patch_size * (c[0] + 0.5), patch_size * (c[1] + 0.5)) for c in coordinates][:len(eq_texts)]
                img = draw_text(
                    text=eq_texts,
                    img_size=(args.image_size, args.image_size),
                    font_size=[8] * len(eq_texts),
                    position=corrdinates
                )
                img.save(f'{args.save_dir}/{number[0]}_{position}.png')

def create_distract_image(args):
    variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    patch_num = args.patch_num // 2 if args.patch_size < 15 else args.patch_num
    patch_size = args.patch_size * 2 if args.patch_size < 15 else args.patch_size
    center_pos = ((patch_num + 1) * patch_num ) // 2

    for number in tqdm(args.digit_set, desc="Creating images", ncols=100):
        for distractor in range(args.distractor_num+1):
            eq_texts = [f'{var}={str}' for var, str in zip(variables, number)]
            for group in range(5):
                rest_positions = random.sample([k for k in range(patch_num ** 2) if k not in [center_pos-1, center_pos, center_pos+1]], 10)
                coordinates = [(patch_num // 2, patch_num // 2)] + [(r % patch_num, r // patch_num) for r in rest_positions]
                corrdinates = [(patch_size * (c[0] + 0.5), patch_size * (c[1] + 0.5)) for c in coordinates][:distractor+1]
                img = draw_text(
                        text=eq_texts,
                        img_size=(args.image_size, args.image_size),
                        font_size=[12] * len(eq_texts),
                        position=corrdinates
                    )
                img.save(f'{args.save_dir}/{number[0]}_{distractor}-{group}.png')

def create_hcut_image(args):
    x_pos = int(args.patch_size * (args.patch_num // 2 + 0.5))
    for number in tqdm(args.digit_set, desc="Creating images", ncols=100):
        # interval 2
        for y_pos in range(args.patch_size//2, args.image_size - args.patch_size//2, 2):
            img = draw_text(
                text=number,
                img_size=(args.image_size, args.image_size),
                font_size=[8],
                position=[(x_pos, y_pos)]
            )
            img.save(f'{args.save_dir}/{number[0]}_{y_pos}.png')

def create_vcut_image(args):
    y_pos = int(args.patch_size * (args.patch_num // 2 + 0.5))
    for number in tqdm(args.digit_set, desc="Creating images", ncols=100):
        # interval 2
        for x_pos in range(args.patch_size//2, args.image_size - args.patch_size//2, 2):
            img = draw_text(
                text=number,
                img_size=(args.image_size, args.image_size),
                font_size=[8],
                position=[(x_pos, y_pos)]
            )
            img.save(f'{args.save_dir}/{number[0]}_{x_pos}.png')


def main(args):

    number_range = 10 ** args.digits

    args.digit_set = generate_unique_numbers(args.digits, args.samples * (args.distractor_num + 1))

    # args.digit_set = [str(i).zfill(args.digits) for i in random.sample(range(number_range), args.samples * (args.distractor_num + 1))]
    args.digit_set = [args.digit_set[i:i+args.distractor_num+1] for i in range(0, len(args.digit_set), args.distractor_num + 1)]

    if args.task == "quality":
        create_quality_image(args)
    elif args.task == "size":
        create_size_image(args)
    elif args.task == "position":
        create_position_image(args)
    elif args.task == "hcut":
        create_hcut_image(args)
    elif args.task == "vcut":
        create_vcut_image(args)
    elif args.task == "distract":
        create_distract_image(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        choices=[
            "instructblip-vicuna-13b",
            "llava-1.5-13b-hf",
            "blip2-flan-t5-xxl",
            "fuyu-8b",
            "Qwen-VL-Chat",
        ],
    )
    parser.add_argument(
        '--task', 
        type=str,
        required=True,
        choices=[
            "quality",
            "size",
            "position",
            "hcut",
            "vcut",
            'distract'
        ]
    )

    parser.add_argument(
        "--digits",
        type=int,
        default=3,
        help="Number of digits",
    )

    parser.add_argument(
        "--distractor_num",
        type=int,
        default=0,
        help="Number of distractor",
    )
    
    args = parser.parse_args()

    if args.model == "instructblip-vicuna-13b" or args.model == "blip2-flan-t5-xxl":
        args.image_size = 224
        args.patch_size = 14
        args.patch_num = 16
    elif args.model == "llava-1.5-13b-hf":
        args.image_size = 336
        args.patch_size = 14
        args.patch_num = 24
    elif args.model == "fuyu-8b":
        args.image_size = 300
        args.patch_size = 30
        args.patch_num = 10
    elif args.model == "Qwen-VL-Chat":
        args.image_size = 448
        args.patch_size = 14
        args.patch_num = 32

    if args.task == "quality" or args.task == "size":
        args.samples = 500
    
    args.center_pos = (args.image_size // 2, args.image_size // 2)
    if args.task == "position" or args.task == "distract" or args.task.find("cut") != -1:
        args.samples = 100
    
    if not os.path.exists(f'./images'):
        os.makedirs(f'./images')

    if args.task != 'quality' and args.task != 'size' and args.task.find("cut") == -1:
        args.save_dir = f'./images/{args.model}/{args.task}_{args.distractor_num}'
    else:
        args.save_dir = f'./images/{args.model}/{args.task}_{args.digits}'
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    main(args)