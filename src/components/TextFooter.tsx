import { Playfair_Display } from "next/font/google";
import Link from "next/link";

const playfairDisplay = Playfair_Display({
  display: "swap",
  subsets: ["latin"],
});

export default function TextFooter() {
  return (
    <>
      {/* Left Text */}
      <h1
        className={`absolute left-10 bottom-5 transform -translate-y-1/2 text-white text-4xl lg:text-5xl font-bold leading-tight ${playfairDisplay.className}`}
      >
        <span className="text-gray-400">Encontre</span> <br /> os pares de fotos
      </h1>

      {/* Right Text */}
      <h1
        className={`absolute right-10 bottom-5 transform -translate-y-1/2 text-white text-4xl lg:text-5xl font-bold leading-tight text-right ${playfairDisplay.className}`}
      >
        e descubra <br /> <span className="text-gray-400">a surpresa</span>
      </h1>
    </>
  );
}
