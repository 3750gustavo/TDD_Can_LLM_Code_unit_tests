local lfs = require("lfs")

-- Function to get last modified time of a file
local function get_last_modified_time(file_path)
    local attributes = lfs.attributes(file_path)
    if attributes then
        return attributes.modification
    end
    return nil
end

-- Function to compare two directories
local function compare_directories(dir1, dir2)
    local report = {
        Passed = true,
        Failed_Count = 0,
        Failed_Tests = {}
    }

    -- Helper function to recursively traverse directories
    local function traverse_directory(directory, base_dir)
        for file in lfs.dir(directory) do
            if file ~= "." and file ~= ".." then
                local file_path = directory .. "/" .. file
                local base_path = base_dir .. "/" .. file

                if lfs.attributes(file_path, "mode") == "directory" then
                    traverse_directory(file_path, base_path)
                else
                    local modified_time1 = get_last_modified_time(directory .. "/" .. file)
                    local modified_time2 = get_last_modified_time(base_dir .. "/" .. file)

                    if modified_time1 and modified_time2 then
                        if modified_time1 < modified_time2 then
                            table.insert(report.Failed_Tests, {
                                Failed_Files = {file},
                                Failure_Location = "dir1"
                            })
                            report.Passed = false
                            report.Failed_Count = report.Failed_Count + 1
                        elseif modified_time1 > modified_time2 then
                            table.insert(report.Failed_Tests, {
                                Failed_Files = {file},
                                Failure_Location = "dir2"
                            })
                            report.Passed = false
                            report.Failed_Count = report.Failed_Count + 1
                        end
                    end
                end
            end
        end
    end

    traverse_directory(dir1, dir2)
    traverse_directory(dir2, dir1)

    return report
end

-- Example usage:
local result = compare_directories("path/to/dir1", "path/to/dir2")

-- Print the result
print("Passed:", result.Passed)
print("Failed Count:", result.Failed_Count)
print("Failed Tests:")
for _, test in ipairs(result.Failed_Tests) do
    print("  Failure Location:", test.Failure_Location)
    print("  Failed Files:")
    for _, file in ipairs(test.Failed_Files) do
        print("    -", file)
    end
end