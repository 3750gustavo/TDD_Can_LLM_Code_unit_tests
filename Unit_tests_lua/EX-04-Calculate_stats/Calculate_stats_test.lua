-- Import the modules
local ChatGPT = require("ChatGPT.calculate_stats")
local CodeLLama = require("CodeLLama.calculate_stats")
local Copilot = require("Copilot.calculate_stats")

-- Define the implementations with their names
local implementations = {
    {ChatGPT, 'ChatGPT'},
    {CodeLLama, 'CodeLLama'},
    {Copilot, 'Copilot'}
}

-- Define the 3 input lists with 3 types of levels of variation in the data
local list1 = {10,9,11,10,8,12,11,9,10,11}
local list2 = {3,9,11,10,8,12,11,9,10,23}
local list3 = {1,19,9,5,2,18,13,7,4,6}

-- Define the expected results
local expected_results = {
    mean = {10.1, 10.6, 8.4},
    stddev = {1.1357816691601,4.7581509013481,6.0033324079215}
}

-- Define the tests
for _, impl in ipairs(implementations) do
    describe("Testing " .. impl[2], function()
        it("should calculate mean correctly", function()
            local results = impl[1](list1, list2, list3)
            for i = 1, #expected_results.mean do
                assert.are.approximately_equal(results.mean[i], expected_results.mean[i], 0.0001)
            end
        end)

        it("should calculate stddev correctly", function()
            local results = impl[1](list1, list2, list3)
            for i = 1, #expected_results.stddev do
                assert.are.approximately_equal(results.stddev[i], expected_results.stddev[i], 0.0001)
            end
        end)
    end)
end