#
# the script asks to specify parameters for NuGrid post-processing
# nucleosynthesis computations for co or ne nova models and starts them
#

die () { 
    echo ""
    echo >&2 "$@"
    echo ""
    exit 1
}

clear

echo ""

if [ $# -eq 0 ]
then
   echo "You must provide a value of the constant neutron density"
   echo "in the form like 3.16d+13!"
   die "Ending..."
else
   denn_value=$1
fi

echo "Selected value of constant neutron density is"
echo $denn_value
echo ""

sed s/denn_value/$denn_value/ ppn_frame.input.template > ppn_frame.input

./ppn.exe 

