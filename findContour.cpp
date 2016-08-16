#include <iostream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
using namespace cv;
using namespace std;
int main(int argc, char** argv)
{
	try
	{
		Mat image,gray,canny,thres,resize;
		vector<vector<Point> > contours;
		int larea = 0, lindex = 0;
		Rect bounding_rect;
		double high_thres, low_thres, a;
		image = imread( argv[1]);
		//cv::resize(image, resize, Size(500,1000),0,0,CV_INTER_LINEAR);
		cvtColor( image, gray, CV_BGR2GRAY);
		blur(gray, gray, Size(3,3));
		high_thres = threshold(gray, thres, 0, 255, CV_THRESH_BINARY | CV_THRESH_OTSU);
		low_thres = high_thres*0.5;
		Canny(gray, canny, low_thres, high_thres);
		findContours(canny, contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE);
		Mat drawing = Mat::zeros( canny.size(), CV_8UC3);
		Scalar color = Scalar(0,0,255);
		for(int i; i<contours.size(); i++)
		{
			a = contourArea(contours[i]);
			if(a>larea)
			{
				larea = a;
				lindex = i;
				bounding_rect = boundingRect(contours[i]);
			}
		}
		cout<< bounding_rect.size() << endl;
		//vector<Point2f> tl_pt = bounding_rect.tl(), br_pt = bounding_rect.br();
		//Mat transmtx = getPerspectiveTransform(tl_pt, br_pt);
		// apply perspective transformation
    //warpPerspective(image, image, transmtx, image.size());
		drawContours(image, contours, lindex, color, 2, 8);
		//rectangle(image, bounding_rect.tl(), bounding_rect.br(), color, 2, 8);
		namedWindow("Contours", CV_WINDOW_NORMAL);
		imshow("Contours", image);
		waitKey(0);
	}
	catch(Exception &e)
	{
		const char* err_msg = e.what();
		cout << "Exception Caught : "<< err_msg << endl;
	}
}
