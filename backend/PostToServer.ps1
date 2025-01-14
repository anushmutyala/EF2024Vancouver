# PostToServer.ps1 - A PowerShell script to send a POST request to a Flask server

# Define the URL of your endpoint
$Url = "http://127.0.0.1:5000/insert_frames"

# Create the JSON payload
$Body = @{
    tools     = @("tool1", "tool2", "tool3")
    action    = "Example Action"
    raw_img   = @{
        key1 = "value1"
        key2 = "value2"
    }
} | ConvertTo-Json -Depth 10

# Define headers
$Headers = @{
    "Content-Type" = "application/json"
}

# Send the POST request
try {
    $Response = Invoke-RestMethod -Uri $Url -Method POST -Headers $Headers -Body $Body
    Write-Host "Response from server:" -ForegroundColor Green
    $Response
} catch {
    Write-Host "Error:" -ForegroundColor Red
    $_
}
