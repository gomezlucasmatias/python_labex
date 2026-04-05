!/bin/bash

echo "Ingresa tu calificación (0-100):"
read calificacion

if [ $calificacion -ge 90 ]; then
    letra="A"
    estado="Excelente ✨"
elif [ $calificacion -ge 80 ]; then
    letra="B"
    estado="Muy bien 👍"
elif [ $calificacion -ge 70 ]; then
    letra="C"
    estado="Bien ✅"
elif [ $calificacion -ge 60 ]; then
    letra="D"
    estado="Suficiente ⚠️"
else
    letra="F"
    estado="Reprobado ❌"
fi

echo ""
echo "📊 Calificación: $calificacion"
echo "📝 Letra: $letra"
echo "🎯 Estado: $estado"

if [ $calificacion -ge 70 ]; then
    echo "🎉 ¡Felicidades, aprobaste!"
else
    echo "😢 Sigue esforzándote, puedes mejorar!"
fi
