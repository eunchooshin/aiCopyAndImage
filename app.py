import os
from openai import OpenAI
import streamlit as st

os.environ['OPENAI_API_KEY'] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ['OPENAI_API_KEY']) 


st.title('홍보 문구 만들기 😎')

keyword = st.text_input('키워드를 입력하세요')

if st.button('생성하기'):
    with st.spinner("생성 중입니다."):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": keyword,
                },
                        {
                    "role": "system",
                    "content": "입력받은 키워드에 대한 솔깃한 홍보 문구 만들어줘",
                }
            ],
            model="gpt-4o",
        )
        response = client.images.generate(
            model="dall-e-3",
            prompt=f"{keyword}, 지브리풍으로 그려줘",
            size="1024x1024",
            quality="standard",
            n=1,
            )
    result = chat_completion.choices[0].message.content
    image_url = response.data[0].url

    st.write(result)
    st.image(image_url)

