import pytest
from triangletype import triangleType
from triangletype import OutOfRangeError

def test_bva_minm_a():
	with pytest.raises(OutOfRangeError):
		triangleType(9, 20, 15)
def test_bva_minm_b():
	with pytest.raises(OutOfRangeError):
		triangleType(20, 9, 15)
def test_bva_minm_c():
	with pytest.raises(OutOfRangeError):
		triangleType(20, 15, 9)

def test_bva_min_a():
	assert triangleType(10, 20, 15) == "Scalene Triangle"
def test_bva_min_b():
	assert triangleType(20, 10, 15) == "Scalene Triangle"
def test_bva_min_c():
	assert triangleType(15, 20, 10) == "Scalene Triangle"

def test_bva_minp_a():
	assert triangleType(11, 20, 15) == "Scalene Triangle"
def test_bva_minp_b():
	assert triangleType(20, 11, 15) == "Scalene Triangle"
def test_bva_minp_c():
	assert triangleType(15, 20, 11) == "Scalene Triangle"

def test_bva_maxm_a():
	assert triangleType(49, 30, 45) == "Scalene Triangle"
def test_bva_maxm_b():
	assert triangleType(30, 49, 45) == "Scalene Triangle"		
def test_bva_maxm_c():
	assert triangleType(45, 30, 49) == "Scalene Triangle"	

def test_bva_max_a():
	assert triangleType(50, 30, 45) == "Scalene Triangle"
def test_bva_max_b():
	assert triangleType(30, 50, 45) == "Scalene Triangle"
def test_bva_max_c():
	assert triangleType(45, 30, 50) == "Scalene Triangle"

def test_bva_maxp_a():
	with pytest.raises(OutOfRangeError):
		triangleType(51, 30, 45)
def test_bva_maxp_b():
	with pytest.raises(OutOfRangeError):
		triangleType(30, 51, 45)
def test_bva_maxp_c():
	with pytest.raises(OutOfRangeError):
		triangleType(30, 45, 51)

def test_bva_nominal():
	assert triangleType(12, 12, 12) == "Equilateral Triangle"
