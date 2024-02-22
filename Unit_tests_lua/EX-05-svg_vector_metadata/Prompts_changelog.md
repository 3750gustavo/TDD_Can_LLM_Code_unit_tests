## svg_dot_product EX 05 versions

# Original Prompt: Write a Lua function that receives as parameter a svg file path and returns the dot product of two vectors in this SVG metadata. If there are no vectors or if they cannot be parsed from the metadata, return -1. The function must be named "svg_dot_product".

## Revisions

1. Write a Lua function named "svg_dot_product" that receives a SVG file path as a parameter. This function should return the dot product of two vectors found within the SVG's <metadata>. The vectors are represented as text content of <vector> elements (e.g., <vector>1,2,3</vector>). If there are fewer than two vectors in the metadata or if they cannot be parsed, the function should return -1
   - Reason: This revision clarifies expectations for the function's input and output, as well as the handling of edge cases.