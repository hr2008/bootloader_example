
#ifndef APP_DATA_H
#define APP_DATRA_H

#define ONE_K	1024U

extern uint32_t _app_start;
extern uint32_t _image_header;

#define APPLICATION_START	(uint32_t)&_app_start
#define APPLICATION_RESET_VECTOR (APPLICATION_START | 0x04U)


#define IMAGE_HEADER 	(uint32_t)&_image_header


typedef struct image_header_t
{
	uint32_t imageMagic;
	uint32_t fwVersion;
	uint32_t APP_SIZE;
	uint8_t  imageHash[32];
}image_header_t;




#endif
