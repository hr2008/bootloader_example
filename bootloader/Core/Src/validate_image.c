
#include "validate_image.h"
#include "app_data.h"
#include "sha256.h"

int compute_hash(uint8_t *hash)
{
	int32_t retVal = -1;
	image_header_t *image_header = (image_header_t*)IMAGE_HEADER;
	mbedtls_sha256_context ctx;

	mbedtls_sha256_init(&ctx);

	mbedtls_sha256_starts_ret(&ctx, 0);

	mbedtls_sha256_update_ret(
		&ctx,
		(const uint8_t *)APPLICATION_START,
		image_header->APP_SIZE);

	mbedtls_sha256_finish_ret(&ctx, hash);

	mbedtls_sha256_free(&ctx);
	return retVal;
}

int verify_app_header()
{
	int32_t retVal = -1;

	return retVal;

}
