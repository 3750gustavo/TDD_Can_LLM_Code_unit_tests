function svg_dot_product(svg_path)
    local file = io.open(svg_path, "r")
    if not file then
        return -1
    end
    
    local metadata = ""
    for line in file:lines() do
        if line:find("<metadata>") then
            metadata = line
            break
        end
    end
    
    file:close()
    
    local vectors = {}
    for vector in metadata:gmatch("<vector>(.-)</vector>") do
        local x, y, z = vector:match("([^,]+),([^,]+),([^,]+)")
        if x and y and z then
            table.insert(vectors, {x = tonumber(x), y = tonumber(y), z = tonumber(z)})
        end
    end
    
    if #vectors < 2 then
        return -1
    end
    
    local dot_product = vectors[1].x * vectors[2].x + vectors[1].y * vectors[2].y + vectors[1].z * vectors[2].z
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

-- To run this code, you can use the following command:
-- lua "Unit_tests_lua\EX-05-svg_vector_metadata\Test_files\Copilot_test.lua"