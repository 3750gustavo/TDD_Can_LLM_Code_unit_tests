function compare_directories(dir1, dir2)
    local report = {
        Passed = true,
        Failed_Count = 0,
        Failed_Tests = {}
    }

    local files1 = {}
    local files2 = {}

    for file in io.popen('ls -1 "'..dir1..'"'):lines() do
        files1[file] = lfs.attributes(dir1..'/'..file, 'modification')
    end

    for file in io.popen('ls -1 "'..dir2..'"'):lines() do
        files2[file] = lfs.attributes(dir2..'/'..file, 'modification')
    end

    for file, mod_date in pairs(files1) do
        if files2[file] then
            if mod_date < files2[file] then
                report.Passed = false
                report.Failed_Count = report.Failed_Count + 1
                table.insert(report.Failed_Tests, {Failed_Files={file}, Failure_Location='dir1'})
            elseif mod_date > files2[file] then
                report.Passed = false
                report.Failed_Count = report.Failed_Count + 1
                table.insert(report.Failed_Tests, {Failed_Files={file}, Failure_Location='dir2'})
            end
        else
            report.Passed = false
            report.Failed_Count = report.Failed_Count + 1
            table.insert(report.Failed_Tests, {Failed_Files={file}, Failure_Location='dir2'})
        end
    end

    for file, mod_date in pairs(files2) do
        if not files1[file] then
            report.Passed = false
            report.Failed_Count = report.Failed_Count + 1
            table.insert(report.Failed_Tests, {Failed_Files={file}, Failure_Location='dir1'})
        end
    end

    return report
end