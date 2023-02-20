# voiceGPT
Voice assistant using chatGPT

### Obtaining session_token (

1. Go to https://chat.openai.com/chat and open the developer tools by `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field.

![image](https://user-images.githubusercontent.com/19218518/206170122-61fbe94f-4b0c-4782-a344-e26ac0d4e2a7.png)

### Requisites installation

```bash
pip install -U pyChatGPT
pip install speech_recognition
pip install gtts
pip install playsound
```
