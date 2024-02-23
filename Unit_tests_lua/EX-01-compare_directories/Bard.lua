function compare_directories(dir1, dir2)
    local report = {
      Passed = true,
      Failed_Count = 0,
      Failed_Tests = {},
    }
  
    -- Check if both directories exist
    if not io.dir(dir1) or not io.dir(dir2) then
      report.Passed = false
      report.Failed_Count = report.Failed_Count + 1
      table.insert(report.Failed_Tests, {
        Failed_Files = {"Both directories"},
        Failure_Location = "N/A",
      })
      return report
    end
  
    -- Helper function to compare file details
    local function compare_files(file1, file2)
      local stat1 = io.stat(dir1 .. "/" .. file1)
      local stat2 = io.stat(dir2 .. "/" .. file2)
  
      -- Check if files exist
      if not stat1 or not stat2 then
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1},
          Failure_Location = stat1 and "dir2" or "dir1",
        })
        return
      end
  
      -- Check file content
      if not io.open(dir1 .. "/" .. file1, "rb") or not io.open(dir2 .. "/" .. file2, "rb") then
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1},
          Failure_Location = "Error reading file content",
        })
        return
      end
      local content1 = io.read("*a")
      local content2 = io.read("*a")
      io.close()
      if content1 ~= content2 then
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1},
          Failure_Location = "Content mismatch",
        })
      end
  
      -- Check file modification dates
      if stat1.mtime ~= stat2.mtime then
        local failure_location = stat1.mtime < stat2.mtime and "dir1" or "dir2"
        report.Passed = false
        report.Failed_Count = report.Failed_Count + 1
        table.insert(report.Failed_Tests, {
          Failed_Files = {file1},
          Failure_Location = failure_location .. " has older modification date",
        })
      end
    end
  
    -- Iterate over files in dir1
    for filename in io.dir(dir1) do
      if filename ~= "." and filename ~= ".." then
        compare_files(filename, filename)
      end
    end
  
    return report
  end  