local function svg_dot_product(svg_file_path)
    -- Open the SVG file and read its contents
    local svg_file = io.open(svg_file_path, "r")
    local svg_contents = svg_file:read("*a")
    svg_file:close()
  
    -- Find the <metadata> element in the SVG contents
    local metadata_start, metadata_end = string.find(svg_contents, "<metadata>")
    if not metadata_start then
      return -1
    end
  
    -- Find the <vector> elements in the metadata
    local vector1_start, vector1_end = string.find(svg_contents, "<vector>", metadata_start)
    local vector2_start, vector2_end = string.find(svg_contents, "<vector>", vector1_end)
    if not vector1_start or not vector2_start then
      return -1
    end
  
    -- Extract the text content of the <vector> elements
    local vector1_text = string.sub(svg_contents, vector1_start + 1, vector1_end - 1)
    local vector2_text = string.sub(svg_contents, vector2_start + 1, vector2_end - 1)
  
    -- Parse the text content as vectors
    local vector1 = {}
    local vector2 = {}
    for i, value in ipairs(string.split(vector1_text, ",")) do
      vector1[i] = tonumber(value)
    end
    for i, value in ipairs(string.split(vector2_text, ",")) do
      vector2[i] = tonumber(value)
    end
  
    -- Calculate the dot product of the vectors
    local dot_product = 0
    for i = 1, #vector1 do
      dot_product = dot_product + vector1[i] * vector2[i]
    end
  
    return dot_product
  end

-- Tests:
-- Define a function to simplify test assertions
local function assertTestResult(testDescription, expected, actual)
    if expected == actual then
        print(testDescription .. " passed")
    else
        print(testDescription .. " failed - Expected: " .. expected .. ", Got: " .. actual)
    end
end

-- Test with SVG having only one vector in <metadata>, expecting -1
local oneVectorSVGPath = [[F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\one_vector.svg]]
local dotProductOneVector = svg_dot_product(oneVectorSVGPath)
assertTestResult("One vector SVG test", -1, dotProductOneVector)

-- Test with an SVG containing an unparsable vector, also expecting -1
local unparsableSVGPath = [[F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\unparsable_vector.svg]]
local dotProductUnparsable = svg_dot_product(unparsableSVGPath)
assertTestResult("Unparsable SVG test", -1, dotProductUnparsable)

-- Test with the given SVG file, expecting the dot product to be 32
local testSVGPath = [[F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\test.svg]]
local dotProductTest = svg_dot_product(testSVGPath)
assertTestResult("Working SVG test", 32, dotProductTest)

-- Performance section
local function performance_test(svg_path, size)
  -- Warm-up
  for i = 1, 100 do
      svg_dot_product(svg_path)
  end
  -- Actual test
  local start_time = os.clock()
  for i = 1, size do
      svg_dot_product(svg_path)
  end
  local end_time = os.clock()
  -- Calculate average runtime in milliseconds
  local total_time = (end_time - start_time) * 1000
  local avg_time = total_time / size
  return avg_time
end

-- Run the tests
io.write("Do you want to run the performance test? (y/n): ")
local run_performance_test = io.read()
if run_performance_test == "y" then
    print("Performance test: ", performance_test(testSVGPath, 100000) .. " milliseconds")
end

-- To run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\CodeLLama_test.lua"