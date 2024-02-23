function compare_directories(dir1, dir2)
    local report = {
        passed = true,
        failed_count = 0,
        failed_tests = {}
    }

    -- Iterate over all files in both directories
    for file in dir1:list_files() do
        local file2 = dir2:list_files()[file.name]
        if file2 then
            -- Check if the files have the same content
            if file.content ~= file2.content then
                report.passed = false
                report.failed_count = report.failed_count + 1
                table.insert(report.failed_tests, {
                    failed_files = {file.name, file2.name},
                    failure_location = dir1.name
                })
            end
        else
            -- File is missing in dir2
            report.passed = false
            report.failed_count = report.failed_count + 1
            table.insert(report.failed_tests, {
                failed_files = {file.name},
                failure_location = dir1.name
            })
        end
    end

    -- Check if all files in dir2 are present in dir1
    for file in dir2:list_files() do
        local file1 = dir1:list_files()[file.name]
        if not file1 then
            report.passed = false
            report.failed_count = report.failed_count + 1
            table.insert(report.failed_tests, {
                failed_files = {file.name},
                failure_location = dir2.name
            })
        end
    end

    return report
end