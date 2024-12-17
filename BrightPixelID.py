#include <stdio.h>
#include <stdint.h>

const int16_t rows = 64;
const int16_t cols = 83;
const int16_t rgb = 3;

const int16_t STARTX = 29;
const int16_t ENDX = 54;

int find_bright_pixels(int img_arr[rows][cols][rgb], int old_img_arr[rows][cols][rgb], int brightness_change_required, int counted_MPs_required);

int find_bright_pixels(int img_arr[rows][cols][rgb], int old_img_arr[rows][cols][rgb], int brightness_change_required, int counted_MPs_required) {
    uint16_t count_bright_pixels = 0;

    // Use res_rows instead of modifying the global rows variable
    for (int16_t i = 0; i < rows; i++) {
        for (int16_t j = STARTX; j < ENDX && j < cols; j++) {  // Ensure j is within res_cols
            int32_t diff = ((int16_t)img_arr[i][j][0] - (int16_t)old_img_arr[i][j][0]) +
                       ((int16_t)img_arr[i][j][1] - (int16_t)old_img_arr[i][j][1]) +
                       ((int16_t)img_arr[i][j][2] - (int16_t)old_img_arr[i][j][2]);
            printf("%d - ", j);
                        printf("%d -- ", i);

            if (diff > brightness_change_required) {
                count_bright_pixels++;
                printf("%d - ", count_bright_pixels);  // Consider removing this print in production
            }
        }
    }

    if (count_bright_pixels > counted_MPs_required) {
        return 1;
    }
    return 0;
}

int main() {
    return 0;
}
