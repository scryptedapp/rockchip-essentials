# Rockchip Essentials

This plugin provides a specialized build of ffmpeg with hardware acceleration on Rockchip VPUs.

To point Scrypted to use Rockchip-accelerated ffmpeg, install this plugin. Set the `SCRYPTED_FFMPEG_PATH` environment variable
to the path listed in the settings. Restart Scrypted.

Hardware accelerated decoders and encoders for H.264 and H.265 are available as `h264_rkmpp` and `hevc_rkmpp`,
respectively. To use, add `-c:v h264_rkmpp` or `-c:v hevc_rkmpp` to the relevant decoder and transcoding
settings.