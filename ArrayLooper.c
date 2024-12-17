#include <stdio.h>
#include <stdint.h>
int rows = 64;
const int cols = 83;
const int rgb = 3;

const int STARTX = 29;
const int ENDX = 54;

int find_bright_pixels(int img_arr[rows][cols][rgb], int old_img_arr[rows][cols][rgb], int brightness_change_required, int counted_MPs_required, int res_rows, int res_cols);

/*
int reduce_resolution(int arr[rows][cols][rgb]) {
    int rows = 64;
    int cols = 83;

    int array[rows][cols];

    // Calculate the new dimensions for the reduced resolution array
    int newRows = rows / 2;
    int newCols = cols / 2;

    // If rows or cols is odd, make sure to round down the new dimensions.
    if (rows % 2 != 0) newRows++;
    if (cols % 2 != 0) newCols++;

    // Create the reduced resolution array
    int reducedArray[newRows][newCols];

    // Merge neighboring cells (average 2x2 blocks)
    for (int i = 0; i < newRows; i++) {
        for (int j = 0; j < newCols; j++) {
            int sum = 0, count = 0;

            // Consider the 2x2 block, making sure not to go out of bounds
            for (int m = i * 2; m < (i * 2 + 2) && m < rows; m++) {
                for (int n = j * 2; n < (j * 2 + 2) && n < cols; n++) {
                    //sum += array[m][n];
                    count++;
                }
            }

            // Store the average in the reduced resolution array
            reducedArray[i][j] = sum / count;
        }
    }

    // Print the reduced resolution array
    printf("The reduced resolution array is:\n");
    for (int i = 0; i < newRows; i++) {
        for (int j = 0; j < newCols; j++) {
            printf("%d ", reducedArray[i][j]);
        }
        printf("\n");
    }

    return 0;
}
*/
int find_bright_pixels(int img_arr[rows][cols][rgb], int old_img_arr[rows][cols][rgb], int brightness_change_required, int counted_MPs_required, int res_rows, int res_cols){
	
    rows = res_rows;
    //cols = res_cols;

	/*
    // Input the number of rows and columns
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printf("Enter the number of columns: ");
    scanf("%d", &cols);
	*/
    //int array[64][83][3] = img_arr;
    //int old_array[64][83][3] = old_img_arr; 
    
    //int compare[64][83][3] = img_arr - old_img_arr;
    uint16_t count_bright_pixels = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = STARTX; j < ENDX; j++) {
            
			/*if(((int)img_arr[i][j][0] - (int)old_img_arr[i][j][0]) + ((int)img_arr[i][j][1] - (int)old_img_arr[i][j][1]) + ((int)img_arr[i][j][2] - (int)old_img_arr[i][j][2]) > brightness_change_required){
				count_bright_pixels++;
                
				}*/
            //printf("%d - ", (int16_t)img_arr[i][j][0]);
			if(((int16_t)img_arr[i][j][0] - (int16_t)old_img_arr[i][j][0]) + ((int16_t)img_arr[i][j][1] - (int16_t)old_img_arr[i][j][1]) + ((int16_t)img_arr[i][j][2] - (int16_t)old_img_arr[i][j][2]) > brightness_change_required){
				count_bright_pixels++;
                
				}
		}
	}
	/*
    // Input elements into the 2D array
    printf("Enter the elements of the 2D array:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("Enter element at [%d][%d]: ", i, j);
            scanf("%d", &array[i][j]);
        }
    }

    // Loop through and print the 2D array
    printf("The elements of the 2D array are:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
    * */
	if (count_bright_pixels > counted_MPs_required){
		return 1;
		}
    return 0;
}

