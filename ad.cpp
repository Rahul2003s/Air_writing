#include<iostream>
#include<unistd.h>
#include<wiringPiI2C.h>

using namespace std;

int main(){

	int fd;
	fd=wiringPiI2CSetup(0x53);

	cout << "Init result:" << fd << endl;
	char buff[6] = {0};
	int x,y,z;

	while(1){
		buf[0]= wiringPiI2CReadReg8(fd, 0x32);
		buf[1]= wiringPiI2CReadReg8(fd, 0x33);

		buf[2]= wiringPiI2CReadReg8(fd, 0x34);
		buf[3]= wiringPiI2CReadReg8(fd, 0x35);

 		buf[4]= wiringPiI2CReadReg8(fd, 0x36);
 		buf[5]= wiringPiI2CReadReg8(fd, 0x37);

		x=((int)buf[1]<<8) | (int)buf[0];
		y=((int)buf[2]<<8) | (int)buf[3];
		z=((int)buf[5]<<8) | (int)buf[4];
		cout<<"x:"<<x<<"\ty:"<<y<<"\tz:"<<z<<endl;
		sleep(1);
	}
	return 0;
}
