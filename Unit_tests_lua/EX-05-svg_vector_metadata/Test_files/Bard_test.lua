local function svg_dot_product(svg_path)
    -- Load the SVG file using LuaXML
    local xml = require("LuaXML")
    local parsed_xml = xml.load(svg_path)
   
    -- Find the <metadata> element
    local metadata = parsed_xml:find("//metadata")
    if not metadata then
      return -1  -- Metadata not found
    end
   
    -- Extract the vectors from <vector> elements
    local vectors = {}
    for vector_element in metadata:children("vector") do
      local vector_text = vector_element:text()
      local numbers = {}
      for number_str in vector_text:gmatch("%d+%.?%d*") do  -- Match numbers with optional decimals
        table.insert(numbers, tonumber(number_str))
      end
      if #numbers > 0 then
        table.insert(vectors, numbers)
      end
    end
   
    if #vectors < 2 then
      return -1  -- Fewer than two vectors found
    end
   
    -- Calculate the dot product
    local v1 = vectors[1]
    local v2 = vectors[2]
    local dot_product = 0
    for i = 1, #v1 do
      dot_product = dot_product + v1[i] * v2[i]
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
-- lua "Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\Bard_test.lua"