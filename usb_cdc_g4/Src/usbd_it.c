#include "main.h"
#include "usbd_it.h"

extern PCD_HandleTypeDef hpcd_USB_FS;

void USB_LP_IRQHandler(void)
{
  HAL_PCD_IRQHandler(&hpcd_USB_FS);
}
