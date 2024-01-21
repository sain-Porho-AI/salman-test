from pydub import AudioSegment
from pydub.silence import split_on_silence

def remove_background_noise(input_path, output_path):
    # Load the audio file
    audio = AudioSegment.from_file(input_path)

    # Set parameters for silence detection
    silence_thresh = audio.dBFS - 10  # Adjust this threshold as needed

    # Split audio on silence
    audio_chunks = split_on_silence(audio, silence_thresh=silence_thresh)

    # Concatenate non-silent chunks
    result = sum(audio_chunks)

    # Export the filtered audio
    result.export(output_path, format="wav")

if __name__ == "__main__":
    input_audio_path = "Recording_22.m4a"  # Replace with your actual file path
    output_audio_path = "output_audio_without_noise.wav"

    remove_background_noise(input_audio_path, output_audio_path)
