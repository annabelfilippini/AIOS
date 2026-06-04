import AppKit
import CoreImage
import CoreImage.CIFilterBuiltins
import Vision

let args = CommandLine.arguments
guard args.count == 3 else {
    fputs("Usage: make_cutout.swift input output\n", stderr)
    exit(2)
}

let inputURL = URL(fileURLWithPath: args[1])
let outputURL = URL(fileURLWithPath: args[2])

guard let inputImage = CIImage(contentsOf: inputURL) else {
    fputs("Could not read input image\n", stderr)
    exit(1)
}

let request = VNGenerateForegroundInstanceMaskRequest()
let handler = VNImageRequestHandler(ciImage: inputImage, options: [:])

do {
    try handler.perform([request])
    guard let result = request.results?.first else {
        fputs("No foreground mask result\n", stderr)
        exit(1)
    }

    let allInstances = IndexSet(result.allInstances)
    let maskBuffer = try result.generateScaledMaskForImage(forInstances: allInstances, from: handler)
    let maskImage = CIImage(cvPixelBuffer: maskBuffer)

    let transparent = CIImage(color: .clear).cropped(to: inputImage.extent)
    let blend = CIFilter.blendWithMask()
    blend.inputImage = inputImage
    blend.backgroundImage = transparent
    blend.maskImage = maskImage

    guard let outputImage = blend.outputImage else {
        fputs("Could not composite output\n", stderr)
        exit(1)
    }

    let context = CIContext(options: [.workingColorSpace: CGColorSpace(name: CGColorSpace.sRGB)!])
    guard let colorSpace = CGColorSpace(name: CGColorSpace.sRGB) else {
        fputs("Could not create color space\n", stderr)
        exit(1)
    }

    try context.writePNGRepresentation(
        of: outputImage,
        to: outputURL,
        format: .RGBA8,
        colorSpace: colorSpace
    )
} catch {
    fputs("Cutout failed: \(error)\n", stderr)
    exit(1)
}
