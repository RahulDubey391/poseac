from videoDownloader import downloadYtVideo, getInputVideoFiles
from modelInitializer import model
from videoPredictor import runPrediction
import argparse
import os

def process_videos(UPLOADS_FOLDER,
                   is_keypoint_file,
                   is_keypoint_video,
                   keypoint_bones):
    try:
        for i in os.listdir(UPLOADS_FOLDER):
            print('[INFO] Running prediction for : %s'%i)

            runPrediction(
                model=model,
                input_video_path=i,
                output_video_path=i,
                is_keypoint_file=is_keypoint_file,
                is_keypoint_video=is_keypoint_video,
                keypoint_bones=keypoint_bones
            )

    except Exception as e:
        raise(e)

def main():
    description = """
                    ##########################
                    #                        #
                    #  Welcome to PoseMaster #
                    #                        #
                    #  Generate keypoint     #
                    #  datasets from Input   #
                    #  Videos for your       #
                    #  upcoming projects     #
                    #  for Human Motion      #
                    #  Synthesis, Animation  #
                    #  References or anything#
                    #                        #
                    ##########################
                """
    
    print(description)

    parser = argparse.ArgumentParser(description=description)
    
    # Add arguments
    parser.add_argument('--YT_LIST_FILE', type=str, help="Input file containing the list of all the youtube videos to be downloaded : Example - yt_list.csv")
    parser.add_argument('--UPLOAD_FOLDER', type=str, help="Target folder to which the videos have to be downloaded : Example - local_uploads")
    parser.add_argument('--is_keypoint_file', action="store_true", default=False, help="The dataset file for each frame. End file is in CSV format")
    parser.add_argument('--is_keypoint_video',action="store_true", default=False, help="Animation utility for generating Videos for the detected keypoints")
    parser.add_argument('--keypoint_bones', action="store_true", default=False, help="Animation utility for rendering Bones for keypoint pairs to mimic Biped structure")
    
    # Parse arguments
    args = parser.parse_args()


    #Initialize the directories
    if not os.path.exists(args.UPLOAD_FOLDER) and not os.path.exists('local_processed'):

        print('[INFO] Creating Directory : %s'%args.UPLOAD_FOLDER)
        os.mkdir(args.UPLOAD_FOLDER)
        print('[INFO] Done!')

        print('[INFO] Creating Directory : local_processed')
        os.mkdir('local_processed')
        print('[INFO] Done!')

    if args.is_keypoint_file:
        if not os.path.exists('local_data'):
            print('[INFO] Creating Directory : local_data')
            os.mkdir('local_data')
            print('[INFO] Done!')

    if args.is_keypoint_video:
        if not os.path.exists('local_keypoint_video'):
            print('[INFO] Creating Directory : local_keypoint_video')
            os.mkdir('local_keypoint_video')
            print('[INFO] Done!')


    #Get the Video Links from the input file
    links = getInputVideoFiles(args.YT_LIST_FILE)

    #Start downloading the Videos
    downloadYtVideo(links, args.UPLOAD_FOLDER)

    #Run Pose Estimator
    process_videos(args.UPLOAD_FOLDER, 
                   is_keypoint_file=args.is_keypoint_file,
                   is_keypoint_video=args.is_keypoint_video,
                   keypoint_bones=args.keypoint_bones)

if __name__ == '__main__':

    main()
