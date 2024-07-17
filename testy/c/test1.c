#include <stdio.h>

// Function to draw a 3D rectangle
void draw3DRectangle(int width, int height, int depth) {
    int i, j, k;

    // Draw the top face
    for (i = 0; i < height; i++) {
        for (j = 0; j < depth + i; j++) {
            printf(" ");
        }
        for (k = 0; k < width; k++) {
            printf("-");
        }
        printf("\n");
    }

    // Draw the front face
    for (i = 0; i < depth; i++) {
        for (j = 0; j < i; j++) {
            printf(" ");
        }
        printf("|");
        for (k = 0; k < width; k++) {
            printf(" ");
        }
        printf("|\n");
    }

    // Draw the bottom face
    for (i = height - 1; i >= 0; i--) {
        for (j = 0; j < depth + i; j++) {
            printf(" ");
        }
        for (k = 0; k < width; k++) {
            printf("-");
        }
        printf("\n");
    }
}

int main() {
    int width = 5;   // Width of the rectangle
    int height = 3;  // Height of the rectangle
    int depth = 4;   // Depth of the rectangle

    // Draw the 3D rectangle
    draw3DRectangle(width, height, depth);

    return 0;
}
