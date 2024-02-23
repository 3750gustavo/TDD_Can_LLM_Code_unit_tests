function compare_directories(dir1, dir2)
    local report = {
        Passed = true,
        Failed_Count = 0,
        Failed_Tests = {}
    }

    -- Get the list of files in dir1
    local files1 = {}
    for file in io.popen('dir /b "'..dir1..'"'):lines() do
        table.insert(files1, file)
    end

    -- Get the list of files in dir2
    local files2 = {}
    for file in io.popen('dir /b "'..dir2..'"'):lines() do
        table.insert(files2, file)
    end

    -- Compare the files in dir1 and dir2
    for _, file in ipairs(files1) do
        if not table.contains(files2, file) then
            report.Passed = false
            report.Failed_Count = report.Failed_Count + 1
            table.insert(report.Failed_Tests, {
                Failed_Files = {file},
                Failure_Location = 'dir1'
            })
        end
    end

    for _, file in ipairs(files2) do
        if not table.contains(files1, file) then
            report.Passed = false
            report.Failed_Count = report.Failed_Count + 1
            table.insert(report.Failed_Tests, {
                Failed_Files = {file},
                Failure_Location = 'dir2'
            })
        end
    end

    return report
end
