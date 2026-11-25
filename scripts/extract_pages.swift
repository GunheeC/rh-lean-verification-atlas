// AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved
// Render existing numbered PDF pages without compiling a document.
import AppKit
import Foundation
import PDFKit
let args=CommandLine.arguments
guard let pdf=PDFDocument(url:URL(fileURLWithPath:args[1])) else {fatalError("Unreadable edition")}
let dir=URL(fileURLWithPath:args[2])
for arg in args.dropFirst(3) {
    guard let n=Int(arg), n>0, let page=pdf.page(at:n-1) else {fatalError("Missing page")}
    try autoreleasepool {
        let size=page.bounds(for:.mediaBox)
        let ratio=1250 / size.width
        let img=page.thumbnail(of:CGSize(width:size.width*ratio,height:size.height*ratio),for:.mediaBox)
        guard let bytes=img.tiffRepresentation, let rep=NSBitmapImageRep(data:bytes),
              let png=rep.representation(using:.png,properties:[:]) else {fatalError("Cannot render page")}
        try png.write(to:dir.appendingPathComponent("p\(n).png"))
    }
}
