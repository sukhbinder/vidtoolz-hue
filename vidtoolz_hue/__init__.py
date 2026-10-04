import vidtoolz
import subprocess
import os


def determine_output_path(input_file, output_file):
    input_dir, input_filename = os.path.split(input_file)
    name, _ = os.path.splitext(input_filename)

    if output_file:
        output_dir, output_filename = os.path.split(output_file)
        if not output_dir:  # If no directory is specified, use input file's directory
            return os.path.join(input_dir, output_filename)
        return output_file
    else:
        return os.path.join(input_dir, f"{name}_hue.mp4")


def create_parser(subparser):
    parser = subparser.add_parser(
        "hue", description="Add a hue to a video using ffmpeg"
    )
    # Add subprser arguments here.
    parser.add_argument("input", type=str, help="Path to the input video file.")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Path to save the output video with the shake effect.",
    )
    parser.add_argument(
        "-st",
        "--start-time",
        type=float,
        required=True,
        help="Start time for the shake effect (in seconds).",
    )
    parser.add_argument(
        "-d",
        "--duration",
        type=float,
        default=1,
        help="Duration for the shake effect (in seconds). Default 1",
    )
    parser.add_argument(
        "-l",
        "--lightening",
        action="store_true",
        help="Add lightening for the hue . Default False",
    )
    return parser


def add_hue_effect(input_file, output_file, start_time, duration, lightening=False):
    # Define the FFmpeg command
    end_time = start_time + duration
    hue = f"hue=s=0:enable='between(t,{start_time},{end_time})'"
    if lightening:
        hue = (
            hue
            + f",eq=brightness=1.0:contrast=2.0:enable='between(t,{start_time},{start_time+0.1})+between(t,{end_time},{end_time-0.1})'"
        )
    command = ["ffmpeg", "-i", input_file, "-vf", hue, "-c:a", "copy", output_file]
    subprocess.run(command)


# ffmpeg -i input.mp4 -vf "hue=s=0:enable='between(t,10,20)'" -c:a copy output.mp4
#  ffmpeg -i input.mp4 -vf "hue=s=0:enable='between(t,1,2)', \
# eq=brightness=1.0:contrast=2.0:enable='between(t,1.0,1.1)+between(t,1.9,2)'" -c:a copy output_flicker.mp4


class ViztoolzPlugin:
    """Add a hue to a video using ffmpeg"""

    __name__ = "hue"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # add actual call here
        output = determine_output_path(args.input, args.output)
        # Call the function to add the shake effect
        add_hue_effect(args.input, output, args.start_time, args.duration, args.lightening)

    def hello(self, args):
        # this routine will be called when "vidtoolz "hue is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


hue_plugin = ViztoolzPlugin()
