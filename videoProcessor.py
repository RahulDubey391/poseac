from utils import GetKeypoint
import numpy as np
import cv2
import os

def extract_keypoint(keypoint):

    try:

        get_keypoint = GetKeypoint()
        
        # nose
        nose_x, nose_y = keypoint[get_keypoint.NOSE]
        # eye
        left_eye_x, left_eye_y = keypoint[get_keypoint.LEFT_EYE]
        right_eye_x, right_eye_y = keypoint[get_keypoint.RIGHT_EYE]
        # ear
        left_ear_x, left_ear_y = keypoint[get_keypoint.LEFT_EAR]
        right_ear_x, right_ear_y = keypoint[get_keypoint.RIGHT_EAR]
        # shoulder
        left_shoulder_x, left_shoulder_y = keypoint[get_keypoint.LEFT_SHOULDER]
        right_shoulder_x, right_shoulder_y = keypoint[get_keypoint.RIGHT_SHOULDER]
        # elbow
        left_elbow_x, left_elbow_y = keypoint[get_keypoint.LEFT_ELBOW]
        right_elbow_x, right_elbow_y = keypoint[get_keypoint.RIGHT_ELBOW]
        # wrist
        left_wrist_x, left_wrist_y = keypoint[get_keypoint.LEFT_WRIST]
        right_wrist_x, right_wrist_y = keypoint[get_keypoint.RIGHT_WRIST]
        # hip
        left_hip_x, left_hip_y = keypoint[get_keypoint.LEFT_HIP]
        right_hip_x, right_hip_y = keypoint[get_keypoint.RIGHT_HIP]
        # knee
        left_knee_x, left_knee_y = keypoint[get_keypoint.LEFT_KNEE]
        right_knee_x, right_knee_y = keypoint[get_keypoint.RIGHT_KNEE]
        # ankle
        left_ankle_x, left_ankle_y = keypoint[get_keypoint.LEFT_ANKLE]
        right_ankle_x, right_ankle_y = keypoint[get_keypoint.RIGHT_ANKLE]
        
        return [
            nose_x, nose_y,
            left_eye_x, left_eye_y,
            right_eye_x, right_eye_y,
            left_ear_x, left_ear_y,
            right_ear_x, right_ear_y,
            left_shoulder_x, left_shoulder_y,
            right_shoulder_x, right_shoulder_y,
            left_elbow_x, left_elbow_y,
            right_elbow_x, right_elbow_y,
            left_wrist_x, left_wrist_y,
            right_wrist_x, right_wrist_y,
            left_hip_x, left_hip_y,
            right_hip_x, right_hip_y,
            left_knee_x, left_knee_y,
            right_knee_x, right_knee_y,        
            left_ankle_x, left_ankle_y,
            right_ankle_x, right_ankle_y
        ]

    except Exception as e:
        raise(e)


def keyPointsToVideo(
        df, 
        plotBones=True,
        output_file_name=None):
    
    try:

        # Define output video filename
        output_video_filename = os.path.join('local_keypoint_video',output_file_name + '.avi') #'output_video.avi'

        # Define codec and frames per second (FPS) for the output video
        codec = cv2.VideoWriter_fourcc(*'XVID')
        fps = 30

        # Get the frame width and height from the DataFrame
        frame_width = int(df['frame_width'].iloc[0])
        frame_height = int(df['frame_height'].iloc[0])

        # Define bones, which are connections between joints
        bones = [('nose', 'left_eye'), ('nose', 'right_eye'), ('left_eye', 'left_ear'),
                ('right_eye', 'right_ear'), ('left_shoulder', 'right_shoulder'),
                ('left_shoulder', 'left_elbow'), ('right_shoulder', 'right_elbow'),
                ('left_elbow', 'left_wrist'), ('right_elbow', 'right_wrist'),
                ('left_shoulder', 'left_hip'), ('right_shoulder', 'right_hip'),
                ('left_hip', 'right_hip'), ('left_hip', 'left_knee'),
                ('right_hip', 'right_knee'), ('left_knee', 'left_ankle'),
                ('right_knee', 'right_ankle')]

        # Create a VideoWriter object to write the video
        out = cv2.VideoWriter(
            output_video_filename, 
            codec, 
            fps, 
            (frame_width, frame_height)
        )

        # Loop through each row of the DataFrame
        for index, row in df.iterrows():

            # Initialize an empty frame
            frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

            # Plot key points on the frame
            for point in ['nose', 'left_eye', 'right_eye', 'left_ear', 'right_ear', 'left_shoulder',
                        'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
                        'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle']:
                
                x_key = point + '_x'
                y_key = point + '_y'
                x = int(row[x_key])
                y = int(row[y_key])
                if x != 0 and y != 0:  # Only plot if x and y coordinates are not zero
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)  # Draw a green circle for each key point

            if plotBones:
                # Draw bones between joints
                for bone in bones:
                    joint1, joint2 = bone
                    x1 = int(row[joint1 + '_x'])
                    y1 = int(row[joint1 + '_y'])
                    x2 = int(row[joint2 + '_x'])
                    y2 = int(row[joint2 + '_y'])
                    if x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:  # Draw bone only if both joints are detected
                        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Draw a red line for each bone

            # Write the frame to the output video
            out.write(frame)

        # Release the VideoWriter object
        out.release()

    except Exception as e:
        raise(e)