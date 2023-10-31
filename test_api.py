import os
import requests
import base64


def test_is_alive():
    response = requests.get(f"{BASE_URL}/is_alive")
    print(response.json())


def test_process_image(image_path, use_base64=True):
    if use_base64:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        data = {"image_data": encoded_image}
    else:
        data = {"image_data": image_path}

    response = requests.post(f"{BASE_URL}/process_image", json=data)
    print(response.content)
    print(response.json())


def test_process_video(video_path):
    with open(video_path, "rb") as video_file:
        encoded_video = base64.b64encode(video_file.read()).decode('utf-8')
    data = {
        "video_data": encoded_video,
        "frame_stride": 10,
        "return_base64": True
    }
    response = requests.post(f"{BASE_URL}/process_video", json=data)
    print(response.json())


if __name__ == "__main__":

    BASE_URL = "http://localhost:8080"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "path_to_json_google_keys.json"


    test_is_alive()
    test_process_image("Screenshot from 2023-10-17 20-59-28.png")
    test_process_video("44.mp4")