-- Function to calculate mean and standard deviation
function calculate_stats(list1, list2, list3)
    -- Function to calculate mean of a list
    local function mean(list)
        local sum = 0
        for _, v in ipairs(list) do
            sum = sum + v
        end
        return sum / #list
    end
    
    -- Function to calculate standard deviation of a list
    local function stddev(list)
        local m = mean(list)
        local sum_squared_diff = 0
        for _, v in ipairs(list) do
            sum_squared_diff = sum_squared_diff + (v - m)^2
        end
        return math.sqrt(sum_squared_diff / #list)
    end
    
    -- Calculate mean and standard deviation for each list
    local stats = {}
    stats['mean'] = {mean(list1), mean(list2), mean(list3)}
    stats['stddev'] = {stddev(list1), stddev(list2), stddev(list3)}
    
    return stats
end