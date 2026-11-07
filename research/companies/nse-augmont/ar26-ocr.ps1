Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null=[Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]
$null=[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation, ContentType=WindowsRuntime]
$null=[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType=WindowsRuntime]
function Await($operation,$resultType) {
 $method=[System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethod -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' } | Select-Object -First 1
 $task=$method.MakeGenericMethod($resultType).Invoke($null,@($operation)); $task.Wait(); $task.Result
}
$engine=[Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
$output=Join-Path $PSScriptRoot 'ar26-ocr.txt'
Set-Content $output ''
Get-ChildItem (Join-Path $PSScriptRoot 'ar26-render') -Filter '*.png' | Sort-Object Name | ForEach-Object {
 $file=Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($_.FullName)) ([Windows.Storage.StorageFile])
 $stream=Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
 $decoder=Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
 $bitmap=Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
 $result=Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
 Add-Content $output ("`n=== " + $_.Name + " ===`n" + $result.Text)
 Write-Output $_.Name
 $stream.Dispose()
}
