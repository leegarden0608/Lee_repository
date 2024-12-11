import requests

url = 'http://34.64.89.66:8080/predict'
image_path = 'local_image.jpg'

with open(image_path, 'rb') as img_file:
    files = {'image': img_file}
    response = requests.post(url, files=files)
    
    # 서버에서 처리된 이미지 다운로드
    if response.status_code == 200:
        with open('result_img.jpg', 'wb') as f:
            f.write(response.content)
        print("결과 이미지 저장됨: predicted_image.jpg")
    else:
        print(f"Error: {response.status_code}, {response.text}")
