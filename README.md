# poseac

Your go-to tool for extracting Estimated Pose Keypoints from Videos in-the-wild!

## About

It's a command-line tool which you can use to run the project. The intention behind creating this project is to enable Developers, Researchers, and Animators to extract Key Point information from raw in-the-wild videos. Further, the dataset extracted can be used for future applications.

## Supported Models
As of now we are just utilizing 1 model for pose-estimation model.
- [https://docs.ultralytics.com/tasks/pose/] YoloV8-Pose

## Applicability

The tool can be used for the following use cases:
- Getting information about movements from detected persons
- Creation of datasets for Human Motion Synthesis/Pose Estimation 3D
- Animators requiring Pose Reference videos
- Any other use case you can suggest

## Usage

## Limitations

As of now, the tool is still under development phase and has the following limitations:
- No documentation for usage
- No support for diverse models
- No pre-processing models/algorithms (Like background removal, upscaling/downscaling, etc...)
- No support for multi-processing (Still under development as of yet)
- Limited to only 2D point estimation (Current model provides a Visible output for z-axis)

## Future Scope

For future developments, we are still working on bringing up the limitations mentioned above to make the tool diverse.

## Contributions

Feel free to raise PR if you can improve the project further. We do require help for the following:
- Support for Multi-Processing
- Model Zoo
- Code Refactoring
- Unit Tests/Integration Tests
- Web-UI for interactive sessions
