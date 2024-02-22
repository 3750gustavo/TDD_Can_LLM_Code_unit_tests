-- Import the math library for mathematical functions
require("math")

-- Define the calculate_stats function
function calculate_stats(list1, list2, list3)
    -- Function to calculate the mean of a list
    local function mean(list)
        local sum = 0
        for i = 1, #list do
            sum = sum + list[i]
        end
        return sum / #list
    end

    -- Function to calculate the standard deviation of a list
    local function stddev(list)
        local m = mean(list)
        local sum_squares = 0
        for i = 1, #list do
            sum_squares = sum_squares + (list[i] - m) ^ 2
        end
        return math.sqrt(sum_squares / #list)
    end

    -- Calculate the mean and standard deviation for each list
    local stats = {
        {
            mean(list1),
            stddev(list1)
        },
        {
            mean(list2),
            stddev(list2)
        },
        {
            mean(list3),
            stddev(list3)
        }
    }

    -- Return the calculated statistics as a dictionary
    return {
        mean = {stats[1][1], stats[2][1], stats[3][1]},
        stddev = {stats[1][2], stats[2][2], stats[3][2]}
    }
end