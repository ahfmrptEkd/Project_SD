# -	Stable Diffusion ��� ���� I2I ���� MVP ����

������ : �ڻ繫��, ������, ���ֿ�, ���ø���, ���缷, �����

---

**������Ʈ �Ⱓ:** 2023.11 ~ 2023.12 (6��)

**������Ʈ Tool:** Flask, Gradio, Stable Diffusion web UI, Github, Notion, Discord


---

<br/>

![video](./asset/video.gif)

<br/>

**Output**
<br>

- **����� (���̺�)**
<p align="center">
	<img src="./asset/outputs/Untitled 10.png" alt="one" width="28%" height="28%" />
	<img src="./asset/outputs/Untitled 11.png" alt="two" width="28%" height="28%" />
	<img src="./asset/outputs/Untitled 12.png" alt="three" width="28%" height="28%" />
 	<figcaption align="center"></figcaption>
</p>

<br>

- **IU**

<p align="center">
	<img src="./asset/outputs/Untitled 13.png" alt="one" width="28%" height="28%" />
	<img src="./asset/outputs/Untitled 14.png" alt="two" width="28%" height="28%" />
	<img src="./asset/outputs/Untitled 15.png" alt="three" width="28%" height="28%" />
	<figcaption align="center"></figcaption>
</p>


<br/>

- **ī���� (Aespa)**

<p align="center">
	<img src="./asset/outputs/Untitled 16.png" alt="one" width="28%" height="28%" />
	<img src="./asset/outputs/Untitled 17.png" alt="two" width="28%" height="28%" />
	<img src="./asset/outputs/Untitled 18.png" alt="three" width="28%" height="28%" />
	<figcaption align="center"></figcaption>
</p>


<br>

### ****������Ʈ ����****

- User �� Image�� �н��� ��, ����ȭ�� ���Ҿ� ���� Image�� ����� ������ ���� AI ��Ʃ��� ������ ������ ����� ������Ʈ
- Minimum Variable Product�� ������ WEB page�� ����� Gradio API ����
- ����ȭ�� ����� LoRA�� �ϴ� training ����
- Stable Diffusion Web UI API�� �̿���  Module Code ����
- ���� Image quality ������ ���� Prompt ����

### ������Ʈ ���

- SNS�� ������������ �α� ���� ��Ʃ��� ������ ����
- ��Ʃ��� �����ʿ� �ҿ�Ǵ� ���� ������ ��ü�� �Ƿ�
- �̹� ��Ÿ ����鵵 �����ϰ� �ִ� AI ���� ����

<br>

### ������Ʈ ��� ����

- **Backend**
    
    <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/>
    
- **Frontend**
    
    Graido
    
- **Tools**
    
    Stable Diffusion Web UI A1111 ![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) ![discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white) ![notion](https://img.shields.io/badge/Notion-%23000000%3Fstyle%3Dsocial%26logo%3Dnotion%26logoColor%3Dblack
)
    
<br>

### ���� �ο�

| �̸�   | ��� ����                                                                                                                                                                                                 |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| �ڻ繫�� | - Base model code ���� <br> - Stable Diffusion�� Ȱ���� model Module code ����<br>- Image Concept�� �´� Prompt Reasearch and Development ���� |
| ������ | - LoRA Reasearch <br> - LoRA training code ����                                     |
| ���ֿ� | - Base Prompt ���� �� Reasearch and Development                                     |
| ����� | - Preprocess �� ������ ����                                     |
| ���缷 | - Web page�� ����� Gradio API ���� <br> - API �� ������ Code ���� <br> - Git Maintance                                     |
| ���ø��� | - �ΰ��� �������̽� Local server�� �̿��� ȯ�� ���� <br> - Flask API�� ����                                     |

<br>

## ������Ʈ ���� ����

1. ������ �̹��� 10���� ���� Easy-Photo�� train �� user�� LoRA �����Ѵ�.
2. ������ LoRA�� ������Ʈ�� �߰��Ѵ�
3. Generation Inference start
4. T2I�� �̹����� ����� ���� �� ������ �� �����Ѵ�.
5. user�� LoRA �� �� ���� �ĺ��� �����Ѵ�.
6. T2I�� output�� I2I�� ó���Ͽ� �̹����� tone-filter �� denoise ��ȭ�۾��� �����Ѵ�.
7. user�� LoRA �� �� ���� �ٽ� �ѹ� �� �ĺ��� �����Ѵ�. (�̹����� denoise�� ���� ���� �κ��� �������� �ϱ� ���ؼ�)
8. I2I�� �ٽ� �ѹ��� ����, ������ �̹����� Denoise�� ���� �ְ�, �ػ󵵸� ���� ���̸鼭 detail up�� �������� upscale �����Ѵ�.
9. �������� �̹����� ������, Graido�� �����Ѵ�.
10. Gradio�� ���� user���� ����Ͽ� �����ݴϴ�.

<br>

![image](./asset/Untitled%209.png)

<br>

### ������Ʈ ��� ���� ����

1. Stable Diffusion T2I, I2I, �׸��� Upscale�� ���� �ڵ� ����
2. �߰����� ��ɵ��� ����� Module ���� 
3. Generated Image quality�� ���� Prompt �� ���� �߰� LoRA �� ����

### ������Ʈ ���� ����

1. **T2I, I2I, Upscale**

![image](./asset/Untitled%208.png)

<br>

1. **T2I** user�� �� �н� user�� �̹����� �޾� �н��� �����Ͽ� LoRA�� �����, ���� ���� Prompt�� ������� ControlNet ����� ���� ������ �������ܿ� Conditioning�� �߰��Ͽ� Pose�� ���� �����մϴ�. ���� Adetailer�� ���� ������ �κ��� Detection model; Yolov8 ���� ���� �󱼰� ���� dection�� �����ϰ�, �����ϴ� �κ� ���� Inpainting ����� ���� inpaint �� �κп� ���� Prompt�� ���� �־�, TextToImg �ܰ迡�� ���� �����մϴ�.

<br>

2. **I2I** ��ȭ �۾� T2I�� output img�� i2i�ܿ����� base img ����� �ξ� ������ �õ��մϴ�. I2I �ܰ迡���� T2I�� �ٸ� Prompt�� �ξ Img�� ������ ������ �ٸ��� �����ϴ°Ϳ� ������ �ΰ� �����մϴ�. ������ Denoise�� ũ�� ���� �ʴ¼������� ������ �õ��մϴ�. ���� T2I������ ����������, Adetailer�� ���� ���� ������ decting�ϰ�, ��׷����� ������ ������ �����մϴ�.

<br>

3. **Upscale** �ػ� ������ ������ �κ� ĳġ I2I�� output img�� �״�� base ������� �ΰ�, denoise�� ���� ���� �����Ѵ�. �׸��� ControlNet�� tile_Resample preprocess ����� ���� �ٽ� ���ø��� �����鼭 �ػ󵵸� �ø��� �۾��� �����մϴ�. Script �ػ󵵸� �ø� �� �������� ������� ����������, webUI ���� script�� Ultrasharp-upscale �� �̿��� �ػ󵵸� �ø��鼭 �������� �κе��� �� �ڿ������� �����ϰԲ� �մϴ�.

<br>


2. **��� Module**

- **Adetailer**
    + �����Ǵ� �̹����� �������� Inpaint ����� �̿��Ͽ� �� �����ϴ� ����� API�� ���� ����.
    + �Ʒ��� 2������ �������� Adetailer �۵����� Image

![image](./asset/4.%20��%20����.png)
![image](./asset/4.%20��%20����2.png)

<br>

- **ControlNet**
    + �Ʒ��� ���� �� ������ pose estimation�� �����ϴ� Image�� Pose�� ���� �����ǰԲ� ��

![image](./asset/pose4.png.png)

![image](./asset/pose_result.png)

<br>

3. **Prompt �� ���� �߰� LoRA �� ����**

- ������Ʈ ���� �پ��� ������ ���� LoRA ���� �� ������ �Ͽ���

![image](./asset/ex10%20detailed%20skin%20����.png)

![image](./asset/ex10%20epicrealism%20�Ⱦ��°�%20������Ʈ��%20������..png)

![image](./asset/90sflesh.png)

![image](./asset/add_detail.png)

![image](./asset/epicrealife.png)

![image](./asset/ex4.png)

![image](./asset/filmvelvia.png)


<br><br>

### ������Ʈ �Ѱ� �� ���� ���

**�Ѱ�**

- ������Ʈ�� �ð��� �����Ͽ� User �� �� �н��Ͽ� ����� LoRA�� ������ ����� �������
- �н��� �ϴ� ������ ���� ���� �ɸ��� �Ѱ谡 ���� ���񽺸� ���� ª�� �ð��ȿ� �����ϴ°��� �������.
- ������Ʈ�� ������ �ν� ������ ���� ����Ͽ� ���ٺ��� �н� �������� ȭ���� ���� ������ õ�������̿���.
- �ڿ��� �����Կ� ���� ���̽� �� fine-tuning ���غ�

**���� ���**

- �����ɸ��� ���񽺸� ���� �α��� ��� �� �̸��Ͽ� User�� �̹����� ������ ���
- Training time�� ���̴� code ����
- ���� image�� �� ���� prompt ����
- Dreambooth�� �̿��� �ǻ� ���̽� �� ����