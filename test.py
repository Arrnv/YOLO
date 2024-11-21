from utils import read_video, save_video
from tracker import Tracker



def main():
    # Read Video
    video_frames = read_video('inputvideos/D35bd9041_1 (25).mp4')

    # Initialize Tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')



if __name__ == '__main__':
    main()