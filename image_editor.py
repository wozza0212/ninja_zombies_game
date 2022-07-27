from PIL import Image

import os

#Create function to flip images round

def rotate_image(input_file_path, output_file_path):
    count=0
    for x in os.listdir(input_file_path):
        path = f'{input_file_path}/{x}'
        original_image = Image.open(path)
        flipped_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        image_name = f'Run__00{count}.png'
        count += 1
        flipped_image.save(f'{output_file_path}/{image_name}')
        original_image.close()
        flipped_image.close()
    print('Done')



        
        

rotate_image('youtube_tutorial/resources/ninjas/move_right', 'youtube_tutorial/resources/ninjas/move_left')
rotate_image('youtube_tutorial/resources/ninjas/jump_right_attack', 'youtube_tutorial/resources/ninjas/jump_left_attack')
rotate_image('youtube_tutorial/resources/ninjas/jump_right', 'youtube_tutorial/resources/ninjas/jump_left')
rotate_image('youtube_tutorial/resources/ninjas/attack_right', 'youtube_tutorial/resources/ninjas/attack_left')
