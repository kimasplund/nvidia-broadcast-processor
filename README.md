# NVIDIA Broadcast Audio Processor

A Python script that allows you to apply NVIDIA Broadcast's audio effects (like Studio Voice, Noise Removal, etc.) to pre-recorded audio and video files. This enables you to enhance your recordings using NVIDIA Broadcast's real-time audio processing features.

## Prerequisites

- Windows 10/11
- NVIDIA Broadcast installed and configured
- [VB-CABLE Virtual Audio Device](https://vb-audio.com/Cable/) installed
- FFmpeg installed and added to system PATH
- Python 3.6 or higher

## Installation

1. Install VB-CABLE:
   - Download from [vb-audio.com/Cable/](https://vb-audio.com/Cable/)
   - Run installer as administrator
   - Restart your computer if required

2. Configure Windows Sound Settings:
   - Right-click the speaker icon in taskbar
   - Select "Open Sound settings"
   - Under "Choose your output device", select "CABLE Input (VB-Audio Virtual Cable)"
   - This ensures all system audio goes through VB-CABLE

3. Configure NVIDIA Broadcast:
   - Open NVIDIA Broadcast
   - In the Microphone section, select "CABLE Output (VB-Audio Virtual Cable)" as input source
   - Enable and configure desired effects (Studio Voice, Noise Removal, etc.)

4. Clone this repository:
   git clone https://github.com/kimasplund/nvidia-broadcast-processor
   cd nvidia-broadcast-processor

## Usage

Basic usage:

python washit.py input_file output.m4a

Example:

python washit.py voice_recording.wav enhanced_voice.m4a

python washit.py podcast_episode.mp4 studio_quality.m4a

Supported input formats:
- WAV (.wav)
- MP4 (.mp4)
- MKV (.mkv)
- AVI (.avi)
- MOV (.mov)

Output is always AAC audio in an M4A container.

## How It Works

1. The script reads the duration of the input file using ffprobe
2. Starts recording from the NVIDIA Broadcast virtual microphone
3. Plays the input file through CABLE Input (which feeds into NVIDIA Broadcast)
4. Records the processed audio from NVIDIA Broadcast with applied effects
5. Automatically stops when playback is complete

## Troubleshooting

1. No audio playing through NVIDIA Broadcast:
   - Verify "CABLE Input (VB-Audio Virtual Cable)" is set as Windows default output device
   - Check NVIDIA Broadcast is using "CABLE Output (VB-Audio Virtual Cable)" as input
   - Test by playing any audio - it should show input levels in NVIDIA Broadcast

2. Recording too short/long:
   - The script adds a 1-second buffer to account for processing delay
   - Make sure no other applications are using NVIDIA Broadcast

3. Poor audio quality:
   - Ensure input file has good quality audio
   - Check NVIDIA Broadcast effect settings
   - Verify CABLE Input/Output sample rates match (should be 48kHz)

4. Effects not being applied:
   - Verify effects are enabled in NVIDIA Broadcast
   - Make sure correct effect settings are configured
   - Check that NVIDIA Broadcast shows audio input levels during playback

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

Kim Asplund
- Email: kim.asplund@gmail.com
- Website: https://asplund.kim

## Acknowledgments

- NVIDIA Broadcast
- VB-Audio for Virtual Cable
- FFmpeg team for media tools
