import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Valentines: Um jogo romantico com proposta surpresa",
  description:
    "Jogue um desafio romatico de cartas e complete todas as fotos para desbloquear a proposta especial.",
  keywords: [
    "jogo dia dos namorados",
    "proposta romantica",
    "desafio de fotos",
    "surpresa dia dos namorados",
    "jogo para casais",
    "cartas romanticas",
    "pedido especial",
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
