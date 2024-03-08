from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Valarie Gaming", page_icon=":video_game:", layout="wide")
def load_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_gaming = "https://lottie.host/fbc3c057-8426-42b1-b9b9-706346bf4d48/QFbYWGyOVk.json"
image_val = Image.open("C:PycharmProjects\pythonProject\pythonProject\images\Valarie gaming.png")

with st.container():
    st.subheader(" 💕'Welcome to Valarie Gaming world'💕 ")
    st.title("The best Gaming Platform around. 100% legit-safe and secure gaming experience.🙂")
    st.write('''Your Ultimate Destination for Non-Stop Fun and Big Wins!
    🎮💰 Join us now and experience the thrill of gaming like never before. Let's play! 🚀
    ''')
    st.write("[Message us>](https://m.me/Valariegaming)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("🎉 Exciting News from Valarie Gaming! 🌟")
        st.write("##")
        st.write('''
    - 💰$2 Redeemable Freeplay! Play Now and Win Big!
    - 🎁Get 100% Bonus on Your First 3 Deposits! Your Winning Streak Starts Here!
    - 🤑Refer a Friend and Get 100% Bonus! Double the Fun, Double the Rewards!
    - 🕒Open 24/7! Your Gaming Adventure Never Sleeps!
    - 🎰Play the Six Most Played Games with High Jackpot Chances:
    ''')

with right_column:
    st_lottie(lottie_gaming, height=250, key="gaming")


st.write("---")
st.subheader("Our games")
st.write("##")
img_column, txt_column = st.columns((1,2))
with img_column:
    st.image(image_val)

with txt_column:
    st.write('''
    - 🔥 [FireKirin>](http://start.firekirin.xyz:8580/index.html)
    - 🌌 [MilkyWay>](https://milkywayapp.xyz/)
    - 🌟 [OrionStars>](http://start.orionstars.vip:8580/index.html)
    - 🐼 [PandaMaster>](https://pandamaster.vip:8888/)
    - 🕹 [GameVault>](https://download.gamevault999.com/)
    - 🌀 [Juwa>](https://dl.juwa777.com/)
    ''')
    st.write('''
    - 🆕 New Big Promos Every Week! Stay Tuned for Exciting Offers!
    - 💸 No Minimum Deposits! Start Playing with Any Amount!
    - 💵 Minimum Cash out: \$35, Maximum: \$300 within 24 Hours! Get Your Winnings Fast!
    - 🔞 18+ Only. Terms and conditions apply.
    
    
    Don't Miss Out on the Ultimate Gaming Experience at Valarie Gaming! Join Now and Win Big! 
    💥Your Ultimate Destination for Non-Stop Fun and Big Wins!
    ''')
