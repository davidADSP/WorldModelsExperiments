for i in `seq 1 8`;
do
  echo worker $i
  python extract.py &
  # sleep 1.0
done
