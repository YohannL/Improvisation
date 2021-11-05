import pytest
import sys
sys.path.append( '..' )
sys.path

from Libs.Model.model import Model

@pytest.fixture
def init_model():
    model = Model()
    return model


def test_model_checkColors(init_model):
    assert "RED" in init_model.colorList 
    assert "BLUE" in init_model.colorList 
    assert "GREEN" in init_model.colorList 
    assert "YELLOW" in init_model.colorList 

def test_model_checkInitStatus(init_model):
    assert "INITIALIZED" is init_model.get_Status()