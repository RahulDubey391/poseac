import cv2
import pandas as pd
from videoProcessor import extract_keypoint, keyPointsToVideo
from utils import dataCols
import os

def runPrediction(model, 
                  input_video_path, 
                  output_video_path,
                  is_keypoint_file=False,
                  is_keypoint_video=False,
                  keypoint_bones=False):
    
    try:
        # Load video
        video_path = os.path.join('local_uploads',input_video_path)
        cap = cv2.VideoCapture(video_path)

        # Define output video writer
        output_path = os.path.join('local_processed',output_video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print('Frame Width, Frame Height --- ',frame_width,frame_height)

        out = cv2.VideoWriter(
            output_path, 
            cv2.VideoWriter_fourcc(*'mp4v'), 
            fps, 
            (frame_width, frame_height)
        )

        frame_no = 0
        dataset_csv = []
        # Process video frame by frame
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform inference
            results = model(frame)

            annotated_frame = results[0].plot()

            # Write the frame to the output video
            out.write(annotated_frame)
            
            results_keypoint = results[0].keypoints.xy.cpu().numpy()
            #results_keypoint = results[0].keypoints.xyn.cpu().numpy()

            #Process Key Points from prediction results
            for result_keypoint in results_keypoint:
                if len(result_keypoint) == 17:
                    keypoint_list = extract_keypoint(result_keypoint)
                    keypoint_list.append(frame_no)
                    keypoint_list.append(frame_width)
                    keypoint_list.append(frame_height)
                    dataset_csv.append(keypoint_list)
            
            frame_no += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release video capture and writer
        cap.release()
        out.release()
        cv2.destroyAllWindows()

        #Store the Keypoints as CSV
        if is_keypoint_file:
            df = pd.DataFrame(
                dataset_csv,
                columns=dataCols
            )

            if '\\' in output_path:
                datafilename = output_path.split('\\')[-1].split('.')[0] + '.csv'
            else: 
                datafilename = output_path.split('/')[-1].split('.')[0] + '.csv'

            df.to_csv( os.path.join('local_data', datafilename), index=False)
            print('Output Kepoints File Shape : ',df.shape)

        #Store the Keypoints as Video
        if is_keypoint_video:
            keyPointsToVideo(
                df=df, 
                plotBones=keypoint_bones,
                output_file_name=output_video_path.split('.')[0]
            )

    except Exception as e:
        raise(e)
