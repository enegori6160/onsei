import azure.cognitiveservices.speech as speechsdk

# speechキー、リージョン、エンドポイント、モデル名を指定すれば使えます
speech_key = ""
service_region = ""

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.endpoint_id = ""
speech_config.speech_synthesis_voice_name = ""
speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio24Khz160KBitRateMonoMp3)

# ユーザーからのテキスト入力を受け取る
text = input("テキストを入力してください: ")

file_name = "{ファイル名}.wav"

file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)

result = speech_synthesizer.speak_text_async(text).get()

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print(f"Speech synthesized for text [{text}], and the audio was saved to [{file_name}]")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print(f"Speech synthesis canceled: {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print(f"Error details: {cancellation_details.error_details}")
