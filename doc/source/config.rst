FILERS2 Config
==============

The following are the configuration options provided by the app. It can be configured by changing appropriate values in the ``config.yaml`` file. The options default to the default value in the classes configurable by these options.

`inspect`: False
 Enables GUI inspection. If True, it is activated by hitting ctrl-e in
 the GUI.

`player_num_cols`: 1
 The number of columns used by the grid displaying all the players.
 If empty, :attr:`player_num_rows` must be set to a number, and then the
 columns will be auto-computed from the number of players added.

`player_num_rows`: None
 The number of rows used by the grid displaying all the players.
 If empty, :attr:`player_num_cols` must be set to a number, and then the
 rows will be auto-computed from the number of players added.


recording
---------


players --- 0
`````````````

`player_name`: "ffmpeg"
 The name of the underlying player used by this player.

`recorder_name`: "video"
 The name of the underlying recorder used by this player.


video_recorder
::::::::::::::

`estimate_record_rate`: False
 Whether to use :attr:`cpl_media.player.BasePlayer.real_rate` for the
 recorder frame rate, as opposed to the one initially provided by the
 player.

`metadata_record`: None
 (internal) Describes the video metadata of the recorder. This is
 the requested format, or best guess of the metadata.
 Read only.

`record_directory`: "E:\msys64\home\matte"
 The directory into which videos should be saved.

`record_fname`: "video{}.mkv"
 The filename to be used to record the next video.
 If ``{}`` is present in the filename, it'll be replaced with the value of
 :attr:`record_fname_count` which auto increments after every video, when
 used.

`record_fname_count`: 0
 A counter that auto increments by one after every recorded video.
 Used to give unique filenames for each video file. See
 :attr:`record_fname`.


thor
::::

`binning_x`: 0
 The x binning value to use.

`binning_x_range`: [0, 0]
 The supported exposure range.

`binning_y`: 0
 The y binning value to use.

`binning_y_range`: [0, 0]
 The supported exposure range.

`black_level`: 0
 The black level value to use.

`black_level_range`: [0, 100]
 The supported exposure range.

`color_gain`: [1, 1, 1]
 The color gain for each red, green, and blue channel.

`exposure_ms`: 0
 The exposure value in ms to use.

`exposure_range`: [0, 100]
 The supported exposure range in ms.

`frame_queue_size`: 1
 The max number of image frames to be allowed on the camera's hardware
 queue. Once exceeded, the frames are dropped.

`freq`: "20 MHz"
 The frequency to use.

`gain`: 0
 The gain value to use.

`gain_range`: [0, 100]
 The supported exposure range.

`metadata_play`: None
 (internal) Describes the video metadata of the video player. This is
 the requested format, or best guess of the metadata.
 Read only.

`metadata_play_used`: None
 (internal) Describes the video metadata of the video player that is
 actually used by the player. This must be set before recorders may allow
 recording the player.
 Depending on the metadata needed by the recorder, it may refuse to
 record until the needed metadata is given.
 Read only.

`num_queued_frames`: 0
 The number of image frames currently on the camera's hardware queue.

`roi_height`: 0
 The height after the y start position of the ROI in pixels, to use.

`roi_width`: 0
 The width after the x start position of the ROI in pixels, to use.

`roi_x`: 0
 The x start position of the ROI in pixels.

`roi_y`: 0
 The y start position of the ROI in pixels.

`sensor_size`: [0, 0]
 The size of the sensor in pixels.

`serial`: ""
 The serial number of the camera that will be opened.

`serials`: []
 The list of serial numbers representing the cameras available.

`supported_freqs`: ['20 MHz']
 The supported frequencies.

`supported_taps`: ['1']
 The supported taps.

`supported_triggers`: ['SW Trigger', 'HW Trigger']
 The trigger types supported by the camera.

`supports_color`: False
 Whether the camera supports color.

`taps`: "1"
 The tap to use.

`trigger_count`: 1
 The number of frames to capture in response to the trigger.

`trigger_type`: "SW Trigger"
 The trigger type of the camera to use.


server_recorder
:::::::::::::::

`max_images_buffered`: 5
 How many images the server should buffer before it starts dropping
 images, rather than queuing them to be sent to the client.

`metadata_record`: None
 (internal) Describes the video metadata of the recorder. This is
 the requested format, or best guess of the metadata.
 Read only.

`port`: 10000
 The server port on which to broadcast the data.

`server`: "localhost"
 The server address on which to broadcast the data.

`timeout`: 0.01
 How long to wait before timing out when reading data before checking the
 queue for other requests.


rtv
:::

`metadata_play`: None
 (internal) Describes the video metadata of the video player. This is
 the requested format, or best guess of the metadata.
 Read only.

`metadata_play_used`: None
 (internal) Describes the video metadata of the video player that is
 actually used by the player. This must be set before recorders may allow
 recording the player.
 Depending on the metadata needed by the recorder, it may refuse to
 record until the needed metadata is given.
 Read only.

`pipe_name`: "RTVPlayer"
 The internal name used to communicate with Barst. When running remotely,
 or if the server already is open, the name is used to discover Barst.

`pixel_fmt`: "gray"
 The pixel format of the images being played.
 It can be one of the keys in :attr:`image_fmts`.

`port`: 0
 The RTV port (camera number) on the card to use.

`remote_computer_name`: ""
 The name of the computer running Barst, if it's a remote computer.
 Otherwise it's the empty string.

`video_fmt`: "full_NTSC"
 The video format of the video being played.
 It can be one of the keys in :attr:`video_fmts`.


ptgray
::::::

`brightness`: {}
 The camera options for the brightness setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`cam_config_opts`: {}
 The configuration options used to configure the camera after opening.
 This are internal and can only be set by the internal thread once
 initially set by config.

`exposure`: {}
 The camera options for the exposure setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`frame_rate`: {}
 The camera options for the frame_rate setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`gain`: {}
 The camera options for the gain setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`gamma`: {}
 The camera options for the gamma setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`hue`: {}
 The camera options for the hue setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`ip`: ""
 The IP address of the camera to open. Either :attr:`ip` or
 :attr:`serial` must be provided.

`iris`: {}
 The camera options for the iris setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`metadata_play`: None
 (internal) Describes the video metadata of the video player. This is
 the requested format, or best guess of the metadata.
 Read only.

`metadata_play_used`: None
 (internal) Describes the video metadata of the video player that is
 actually used by the player. This must be set before recorders may allow
 recording the player.
 Depending on the metadata needed by the recorder, it may refuse to
 record until the needed metadata is given.
 Read only.

`mirror`: False
 Whether the camera is mirrored. Read only.

`pan`: {}
 The camera options for the pan setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`saturation`: {}
 The camera options for the saturation setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`serial`: 0
 The serial number of the camera to open. Either :attr:`ip` or
 :attr:`serial` must be provided.

`sharpness`: {}
 The camera options for the sharpness setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`shutter`: {}
 The camera options for the shutter setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.

`tilt`: {}
 The camera options for the tilt setting.
 This may only be set by calling :meth:`ask_cam_option_config`, not
 set directly.


network_client
::::::::::::::

`metadata_play`: None
 (internal) Describes the video metadata of the video player. This is
 the requested format, or best guess of the metadata.
 Read only.

`metadata_play_used`: None
 (internal) Describes the video metadata of the video player that is
 actually used by the player. This must be set before recorders may allow
 recording the player.
 Depending on the metadata needed by the recorder, it may refuse to
 record until the needed metadata is given.
 Read only.

`port`: 0
 The server port that broadcasts the data.

`server`: ""
 The server address that broadcasts the data.

`timeout`: 0.01
 How long to wait before timing out when reading data before checking the
 queue for other requests.


image_file_recorder
:::::::::::::::::::

`compression`: "raw"
 Whether to compress when :attr:`extension` is `tiff`. Can be one of
 ``'raw', 'lzw', 'zip'``.

`extension`: "tiff"
 The extension of the images being saved.

`metadata_record`: None
 (internal) Describes the video metadata of the recorder. This is
 the requested format, or best guess of the metadata.
 Read only.

`record_directory`: "E:\msys64\home\matte"
 The directory into which videos should be saved.

`record_prefix`: "image_"
 The prefix to the filename of the images being saved.


ffmpeg
::::::

`dshow_filename`: ""
 The name of the dshow camera to open.

`dshow_opt`: ""
 The camera options associated with :attr:`dshow_true_filename` when
 dshow is used.

`dshow_rate`: 0
 The frame rate to request from the dshow camera.

`dshow_true_filename`: ""
 The real and complete filename of the direct show (webcam) device.

`file_fmt`: ""
 The format used to play the video. Can be empty or a format e.g.
 ``mjpeg`` for webcams.

`icodec`: ""
 The codec used to open the video stream with if it needs to be
 specified for the camera.

`metadata_play`: None
 (internal) Describes the video metadata of the video player. This is
 the requested format, or best guess of the metadata.
 Read only.

`metadata_play_used`: None
 (internal) Describes the video metadata of the video player that is
 actually used by the player. This must be set before recorders may allow
 recording the player.
 Depending on the metadata needed by the recorder, it may refuse to
 record until the needed metadata is given.
 Read only.

`play_filename`: ""
 The filename of the media being played. Can be e.g. a filename etc.

`use_dshow`: True
 Whether we use dshow - i.e. USB webcams, or normal media sources.

